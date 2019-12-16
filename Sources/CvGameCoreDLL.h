#pragma once

#ifndef CvGameCoreDLL_h__
#define CvGameCoreDLL_h__

//
// includes (pch) for gamecore dll files
// Author - Mustafa Thamer
//

//
// WINDOWS
//
#pragma warning( disable: 4530 )	// C++ exception handler used, but unwind semantics are not enabled

//#ifdef __INTELLISENSE__
//// #undef _MSC_VER
//#define _MSC_VER 1310
//#define BOOST_MSVC 1310
//#define boost155_MSVC 1310
//#define BOOST_FUNCTION_PARMS
//#define BOOST_FUNCTION_PARM
//#define BOOST_PP_VARIADICS 0
//#endif

#define NOMINMAX
#define _WIN32_WINNT 0x0600
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <MMSystem.h>

//#if defined _DEBUG && !defined USE_MEMMANAGER
//#define USE_MEMMANAGER
//#include <crtdbg.h>
//#endif
//#if !defined USE_MEMMANAGER
//#define USE_MEMMANAGER
//#endif

//
// Standard headers
//
#include <vector>
#include <list>
#include <tchar.h>
#include <math.h>
#include <assert.h>
#include <map>
#define _SILENCE_STDEXT_HASH_DEPRECATION_WARNINGS
#include <hash_map>
#include <hash_set>
#include <stdio.h>
#include <utility>
#include <algorithm>
#include <set>
#include <fstream>

//
// Google sparsehash
//
#include <sparsehash/sparse_hash_set>
#include <sparsehash/sparse_hash_map>
#include <sparsehash/dense_hash_set>
#include <sparsehash/dense_hash_map>
#include <sparsehash/template_util.h>
#include <sparsehash/type_traits.h>


#define DllExport   __declspec( dllexport ) 

#include "EnumFlags.h"
#include "NiPoint.h"
#include "hash.h"

//
// Polyfills
//
#include "nullptr_t.h"
#include "algorithm2.h"

//
// Basic types
//
typedef unsigned char    byte;
typedef unsigned short   word;
typedef unsigned int     uint;
typedef unsigned long    dword;
typedef unsigned __int64 qword;
typedef wchar_t          wchar;

//
// Type traits
//
#define MAX_CHAR                            (0x7f)
#define MIN_CHAR                            (0x80)
#define MAX_SHORT                           (0x7fff)
#define MIN_SHORT                           (0x8000)
#define MAX_INT                             (0x7fffffff)
#define MIN_INT                             (0x80000000)
#define MAX_UNSIGNED_CHAR                   (0xff)
#define MIN_UNSIGNED_CHAR                   (0x00)
#define MAX_UNSIGNED_SHORT                  (0xffff)
#define MIN_UNSIGNED_SHORT                  (0x0000)
#define MAX_UNSIGNED_INT                    (0xffffffff)
#define MIN_UNSIGNED_INT                    (0x00000000)

#define SAFE_DELETE(p)       { if(p) { delete (p);     (p)=NULL; } }
#define SAFE_DELETE_ARRAY(p) { if(p) { delete[] (p);   (p)=NULL; } }
#define SAFE_RELEASE(p)      { if(p) { (p)->Release(); (p)=NULL; } }

#define SQR(x)      ( (x) * (x) )
#define DEGTORAD(x) ( (float)( (x) * (M_PI / 180) ))
#define LIMIT_RANGE(low, value, high) value = (value < low ? low : (value > high ? high : value));
#define M_PI       3.14159265358979323846
#define fM_PI		3.141592654f		//!< Pi (float)

// cppcheck-suppress invalidPointerCast
__forceinline DWORD FtoDW( float f ) { return *(DWORD*)&f; }
// cppcheck-suppress invalidPointerCast
__forceinline float DWtoF( dword n ) { return *(float*)&n; }
__forceinline float MaxFloat() { return DWtoF(0x7f7fffff); }

// General flags that declare cache access
struct ECacheAccess
{
	enum flags
	{
		None = 0,
		Read = 1 << 0,
		Write = 1 << 1,
		ReadWrite = Read | Write
	};
};
DECLARE_FLAGS(ECacheAccess::flags);

//
// Feature macros
//
// #define STRENGTH_IN_NUMBERS
//
// Cache feature macros
//
#define PATHFINDING_CACHE
#define PATHFINDING_VALIDITY_CACHE
#define DISCOVERY_TECH_CACHE

//
// Profiler
//
#ifdef USE_INTERNAL_PROFILER
#define MEMTRACK
#endif

void startProfilingDLL(bool longLived);
void stopProfilingDLL(bool longLived);
//#define USE_INTERNAL_PROFILER
//#define FP_PROFILE_ENABLE
#ifdef USE_INTERNAL_PROFILER
extern bool g_bTraceBackgroundThreads;

struct ProfileSample;
struct ProfileLinkageInfo;
void IFPProfileThread();
bool IFPIsMainThread();
void IFPBeginSample(ProfileLinkageInfo* linkageInfo, bool bAsConditional = false);
void IFPEndSample(ProfileLinkageInfo* linkageInfo, bool bAsConditional = false);
void IFPCancelSample(ProfileLinkageInfo* linkageInfo);
void dumpProfileStack();
void EnableDetailedTrace(bool enable);
void IFPSetCount(ProfileSample* sample, int count);
#endif

#define	MEMORY_TRACK()
#define MEMORY_TRACK_EXEMPT()
#define MEMORY_TRACE_FUNCTION()
#define MEMORY_TRACK_NAME(x)

//
// Python
//
#ifdef _DEBUG
  #undef _DEBUG
  #include "Python.h"
  #define _DEBUG
#else
  #include "Python.h"
#endif

//
// Boost
//
#define BOOST_155_USE_WINDOWS_H
#include <boost155/scoped_ptr.hpp>
#include <boost155/scoped_array.hpp>
#include <boost155/shared_ptr.hpp>
#include <boost155/shared_array.hpp>
#include <boost155/lambda/lambda.hpp>
#include <boost155/bind.hpp>
#include <boost155/optional.hpp>
#include <boost155/algorithm/string.hpp>
#include <boost155/format.hpp>
#include <boost155/function.hpp>
#include <boost155/array.hpp>
#include <boost155/utility.hpp>
#include <boost155/foreach.hpp>
#include <boost155/range.hpp>
#include <boost155/range/adaptor/filtered.hpp>
#include <boost155/range/adaptor/transformed.hpp>
using namespace boost155::adaptors;
#include <boost155/range/any_range.hpp>
#include <boost155/range/algorithm.hpp>
 

// Make boost foreach look nice enough to actually use
#define foreach_ BOOST_155_FOREACH
// Alias our latest boost version
namespace bst = boost155;
// Bring range adaptors straight into global namespace, as we use them a lot
//using namespace bst::adaptors;

//
// Boost Python
//
#ifndef __INTELLISENSE__
// Disable the boost 1.32 placeholders, we won't be using them
#define BOOST_BIND_NO_PLACEHOLDERS
#include <boost/python/list.hpp>
#include <boost/python/tuple.hpp>
#include <boost/python/class.hpp>
#include <boost/python/manage_new_object.hpp>
#include <boost/python/return_value_policy.hpp>
#include <boost/python/object.hpp>
#include <boost/python/def.hpp>
#include <boost/python/enum.hpp>
namespace python = boost::python;
#endif

//#include <boost155/range/adaptor/filtered.hpp>
//#include <boost155/range/adaptor/transformed.hpp>

//
// xercesc for XML loading
// 
#include <xercesc/dom/DOM.hpp>
#include <xercesc/util/XMLString.hpp>
#include <xercesc/util/PlatformUtils.hpp>
#include <xercesc/parsers/XercesDOMParser.hpp>
#include <xercesc/sax/SAXException.hpp>
#include <xercesc/sax/HandlerBase.hpp>
#include <xercesc/sax/SAXException.hpp>
#include <xercesc/sax/HandlerBase.hpp>
#include <xercesc/framework/MemBufInputSource.hpp>
#include <xercesc/framework/XMLGrammarPoolImpl.hpp>
#include <xercesc/framework/Wrapper4InputSource.hpp>
#include <xercesc/validators/common/Grammar.hpp>


//
// Json
//
#include "picojson.h"


//
// Our code
//
#include "copy_iterator.h"
#include "index_iterator_base.h"
#include "logging.h"

#include "CvAllocator.h"

#include "FAssert.h"
#include "CheckSum.h"
#include "Stopwatch.h"
#include "CvGameCoreDLLDefNew.h"
#include "FDataStreamBase.h"
#include "FFreeListArrayBase.h"
#include "FFreeListTrashArray.h"
#include "FFreeListArray.h"
#include "FVariableSystem.h"
#include "FAStarNode.h"
#include "CvString.h"
#include "CvEnums.h"
#include "CvStructs.h"
#include "CvDLLUtilityIFaceBase.h"
#include "CvDLLEngineIFaceBase.h"
#include "CvDLLFAStarIFaceBase.h"
#include "CvDLLPythonIFaceBase.h"
#include "CvDLLInterfaceIFaceBase.h"
#include "CvDLLXMLIFaceBase.h"

#include "CvGameCoreUtils.h"
#include "CvXMLLoadUtility.h"
#include "CvInitCore.h"
#include "CvArtFileMgr.h"
#include "CvGameTextMgr.h"
#include "CvBugOptions.h"
#include "CvPopupInfo.h"
#include "CvEventReporter.h"
#include "CvMessageControl.h"
#include "CvDiploParameters.h"
#include "CvDeal.h"
#include "CvInfoWater.h"
#include "CvMap.h"
#include "CvViewport.h"
#include "CvGlobals.h"
#include "CvGameAI.h"
#include "CvTeamAI.h"
#include "CvPlayerAI.h"
#include "CvCityAI.h"
#include "CvUnitAI.h"
#include "CvSelectionGroupAI.h"
#include "CvPlot.h"
#include "CvTalkingHeadMessage.h"
#include "FProfiler.h"
#include "CvPathGenerator.h"
#include "CvBugOptions.h"
#include "CvPython.h"

#include "SCvDebug.h"
#include "SCvInternalGlobals.h"

#include "CyGlobalContext.h"
#include "CyArtFileMgr.h"
#include "CyDeal.h"
#include "CyMap.h"
#include "CyArea.h"
#include "CyGame.h"
#include "CyTeam.h"
#include "CyPlayer.h"
#include "CyCity.h"
#include "CyUnit.h"
#include "CySelectionGroup.h"
#include "CyPlot.h"

#ifdef FINAL_RELEASE
// Undefine OutputDebugString in final release builds
#undef OutputDebugString
#define OutputDebugString(x)
#endif //FINAL_RELEASE

#endif // CvGameCoreDLL_h__
