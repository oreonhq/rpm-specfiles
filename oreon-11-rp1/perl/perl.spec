%global source0_hash 505cf43912e9480495c344c70260452e32aa2a73c546a026b3f100053b23ce91
%global perl_version    5.44.0
%global perl_epoch      4
%global perl_arch_stem -thread-multi
%global perl_archname %{_arch}-%{_os}%{perl_arch_stem}
%global multilib_64_archs aarch64 %{power64} s390x sparc64 x86_64 
%global parallel_tests 1
%global tapsetdir   %{_datadir}/systemtap/tapset
%global dual_life 0
%bcond_with perl_bootstrap
%if %{with perl_bootstrap}
%define gendep_file %(find . -name gendep.macros -print -quit 2>/dev/null)
%include %{gendep_file}
%global perl_bootstrap 1
%endif
%global rebuild_from_scratch %{defined perl_bootstrap}
%global __provides_exclude_from .*%{_docdir}
%if %{defined perl_archlib}
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}.*%{perl_archlib}/.*\\.pl$|.*%{perl_privlib}/.*\\.pl$
%endif
%global __requires_exclude_from %{_docdir}
%global __provides_exclude perl\\((VMS|Win32|BSD::|DB\\)$)
%global __requires_exclude perl\\((VMS|BSD::|Win32|Tk|Mac::|Your::Module::Here)
%global perl5_testdir   %{_libexecdir}/perl5-tests
%bcond_without perl_enables_cplusplus_test
%bcond_without bdb
%bcond_without gdbm
%bcond_without perl_enables_groff
%bcond_without perl_enables_turkish_test
%bcond_with perl_enables_syslog_test
%bcond_without perl_enables_systemtap
%bcond_with perl_enables_tcsh
%bcond_without test
%undefine _package_note_file
Name:           perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          %{perl_epoch}
Version:        %{perl_version}
Release:        1%{?dist}
Summary:        Practical Extraction and Report Language
Url:            https://www.perl.org/
Source0:        https://www.cpan.org/src/5.%{dual_life}/%{name}-%{version}.tar.xz
Source3:        macros.perl
Source4:        perl.stp
Source5:        perl-example.stp
Source6:        Pod-Html-license-clarification
Source7:        gendep.macros
Source8:        config.over
Patch1:         perl-perlbug-tag.patch
Patch2:         perl-5.8.0-libdir64.patch
Patch3:         perl-5.10.0-libresolv.patch
Patch4:         perl-USE_MM_LD_RUN_PATH.patch
Patch5:         perl-5.22.1-Provide-ExtUtils-MM-methods-as-standalone-ExtUtils-M.patch
Patch6:         perl-5.10.0-x86_64-io-test-failure.patch
Patch7:         perl-5.14.1-offtest.patch
Patch8:         perl-5.16.3-create_libperl_soname.patch
Patch9:         perl-5.22.0-Install-libperl.so-to-shrpdir-on-Linux.patch
Patch10:        perl-5.34.0-Destroy-GDBM-NDBM-ODBM-SDBM-_File-objects-only-from-.patch
Patch11:        perl-5.22.1-Replace-EU-MM-dependnecy-with-EU-MM-Utils-in-IPC-Cmd.patch
Patch12:        perl-5.27.8-hints-linux-Add-lphtread-to-lddlflags.patch
Patch13:        perl-5.28.0-Pass-CFLAGS-to-dtrace.patch
Patch14:        perl-makedep.patch
Patch200:       perl-5.16.3-Link-XS-modules-to-libperl.so-with-EU-CBuilder-on-Li.patch
Patch201:       perl-5.16.3-Link-XS-modules-to-libperl.so-with-EU-MM-on-Linux.patch
Patch202:       perl-5.36.0-Add-definition-of-OPTIMIZE-to-.ph-files.patch
%if %{with gdbm}
%endif
%if %{with perl_enables_groff}
%endif
%if %{with bdb}
%endif
%if !%{defined perl_bootstrap}
%endif
%if %{with perl_enables_systemtap}
%endif
%if %{with perl_enables_tcsh}
%endif
%if %{with test}
%if %{with perl_enables_cplusplus_test}
%endif
%if %{with perl_enables_turkish_test}
%endif
%if %{with perl_enables_syslog_test}
%endif
%endif
%global perl_compat perl(:MODULE_COMPAT_5.42.2)
Requires:       %perl_compat
Requires:       perl-interpreter%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-libs%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-devel%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl-macros
Requires:       perl-utils
%if %{defined perl_bootstrap}
%gendep_perl
%endif
Requires:       perl-Archive-Tar, perl-Attribute-Handlers, perl-autodie,
Requires:       perl-AutoLoader, perl-AutoSplit, perl-autouse,
Requires:       perl-B, perl-base, perl-Benchmark, perl-bignum, perl-blib,
Requires:       perl-Carp, perl-Class-Struct,
Requires:       perl-Compress-Raw-Bzip2, perl-Compress-Raw-Zlib,
Requires:       perl-Config-Extensions, perl-Config-Perl-V, perl-constant,
Requires:       perl-CPAN, perl-CPAN-Meta, perl-CPAN-Meta-Requirements,
Requires:       perl-CPAN-Meta-YAML, perl-Data-Dumper,
%if %{with bdb}
Requires:       perl-DB_File,
%endif
Requires:       perl-DBM_Filter, perl-debugger, perl-deprecate,
Requires:       perl-Devel-Peek, perl-Devel-PPPort, perl-Devel-SelfStubber,
Requires:       perl-diagnostics, perl-Digest, perl-Digest-MD5, perl-Digest-SHA,
Requires:       perl-DirHandle,
Requires:       perl-doc,
Requires:       perl-Dumpvalue,
Requires:       perl-DynaLoader,
Requires:       perl-Encode, perl-Encode-devel, perl-encoding,
Requires:       perl-encoding-warnings, perl-English,
Requires:       perl-Env, perl-Errno, perl-experimental, perl-Exporter,
Requires:       perl-ExtUtils-CBuilder, perl-ExtUtils-Constant,
Requires:       perl-ExtUtils-Command,
Requires:       perl-ExtUtils-Embed, perl-ExtUtils-Install,
Requires:       perl-ExtUtils-MakeMaker, perl-ExtUtils-Manifest,
Requires:       perl-ExtUtils-Miniperl, perl-ExtUtils-MM-Utils,
Requires:       perl-ExtUtils-ParseXS,
Requires:       perl-Fcntl, perl-fields,
Requires:       perl-File-Basename, perl-File-Compare, perl-File-Copy,
Requires:       perl-File-DosGlob, perl-File-Fetch,
Requires:       perl-File-Find, perl-File-Path, perl-File-stat, perl-File-Temp,
Requires:       perl-FileCache, perl-FileHandle, perl-filetest,
Requires:       perl-Filter, perl-Filter-Simple,
Requires:       perl-FindBin,
%if %{with gdbm}
Requires:       perl-GDBM_File,
%endif
Requires:       perl-Getopt-Long, perl-Getopt-Std,
Requires:       perl-Hash-Util, perl-Hash-Util-FieldHash, perl-HTTP-Tiny,
Requires:       perl-if, perl-IO, perl-IO-Compress, perl-IO-Socket-IP,
Requires:       perl-IO-Zlib, perl-IPC-Cmd, perl-IPC-Open3, perl-IPC-SysV,
Requires:       perl-I18N-Collate, perl-I18N-Langinfo, perl-I18N-LangTags,
Requires:       perl-JSON-PP,
Requires:       perl-less,
Requires:       perl-lib, perl-libnet, perl-libnetcfg,
Requires:       perl-locale, perl-Locale-Maketext, perl-Locale-Maketext-Simple,
Requires:       perl-Math-BigInt, perl-Math-BigInt-FastCalc,
Requires:       perl-Math-Complex, perl-Memoize, perl-meta-notation,
Requires:       perl-MIME-Base64,
Requires:       perl-Module-CoreList, perl-Module-CoreList-tools,
Requires:       perl-Module-Load, perl-Module-Load-Conditional,
Requires:       perl-Module-Loaded, perl-Module-Metadata,
Requires:       perl-mro,
%if %{with gdbm}
Requires:       perl-NDBM_File,
%endif
Requires:       perl-Net, perl-Net-Ping, perl-NEXT,
%if %{with gdbm}
Requires:       perl-ODBM_File,
%endif
Requires:       perl-Opcode, perl-open, perl-overload, perl-overloading,
Requires:       perl-parent, perl-PathTools, perl-Params-Check, perl-perlfaq,
Requires:       perl-PerlIO-via-QuotedPrint, perl-Perl-OSType,
Requires:       perl-ph,
Requires:       perl-Pod-Checker, perl-Pod-Escapes, perl-Pod-Functions,
Requires:       perl-Pod-Html, perl-Pod-Perldoc,
Requires:       perl-Pod-Simple, perl-Pod-Usage, perl-podlators, perl-POSIX,
Requires:       perl-Safe, perl-Scalar-List-Utils,
Requires:       perl-Search-Dict, perl-SelectSaver,
Requires:       perl-SelfLoader, perl-sigtrap, perl-Socket, perl-sort,
Requires:       perl-Storable,
Requires:       perl-subs,
Requires:       perl-Symbol, perl-Sys-Hostname, perl-Sys-Syslog,
Requires:       perl-Term-ANSIColor, perl-Term-Cap, perl-Term-Complete,
Requires:       perl-Term-ReadLine, perl-Term-Table,
Requires:       perl-Test, perl-Test-Harness, perl-Test-Simple,
Requires:       perl-Text-Abbrev, perl-Text-Balanced, perl-Text-ParseWords,
Requires:       perl-Text-Tabs+Wrap,
Requires:       perl-Thread, perl-Thread-Queue, perl-Thread-Semaphore,
Requires:       perl-threads, perl-threads-shared,
Requires:       perl-Tie, perl-Tie-File, perl-Tie-Memoize, perl-Tie-RefHash,
Requires:       perl-Time, perl-Time-HiRes, perl-Time-Local, perl-Time-Piece,
Requires:       perl-Unicode-Collate, perl-Unicode-Normalize, perl-Unicode-UCD,
Requires:       perl-User-pwent,
Requires:       perl-vars, perl-version, perl-vmsish,
Provides:       perl-core = %{perl_version}-%{release}
Provides:       perl-core%{?_isa} = %{perl_version}-%{release}
Obsoletes:      perl-core < 5.26.0-395
Provides:       perl(dumpvar.pl)
Provides:       perl(PerlIO::scalar)
Provides:       perl(Pod::Functions)
Provides:       perl(Pod::Html)
Provides:       perl(Tie::Array)
Provides:       perl(Tie::Handle)
Provides:       perl(Tie::Hash)
Provides:       perl(Tie::Scalar)
Provides:       perl(Tie::StdArray)
Provides:       perl(Tie::StdHash)
Provides:       perl(Tie::StdScalar)
Provides:       perl(Time::Seconds)
Provides:       perl(Time::Piece)
Provides:       perl(UNIVERSAL)
Provides:       perl(Unicode::UCD)
Provides:       perl(attributes)
Provides:       perl(charnames)
Provides:       perl(deprecate)
Provides:       perl(fields)
Provides:       perl(less)
Provides:       perl(overloading)
Provides:       perl(perl5db.pl)
Provides:       perl(sigtrap)
Provides:       perl(sort)
Provides:       perl(subs)
Provides:       perl(warnings::register)
Provides:       perl(base)
Provides:       perl(AnyDBM_File)
Provides:       perl(Attribute::Handlers)
Provides:       perl(AutoLoader)
Provides:       perl(AutoSplit)
Provides:       perl(B::Concise)
Provides:       perl(Benchmark)
Provides:       perl(CPAN)
Provides:       perl(Class::Struct)
Provides:       perl(DB)
Provides:       perl(Devel::Peek)
Provides:       perl(DirHandle)
Provides:       perl(Dumpvalue)
Provides:       perl(English)
Provides:       perl(ExtUtils::Command)
Provides:       perl(ExtUtils::Constant)
Provides:       perl(ExtUtils::Embed)
Provides:       perl(ExtUtils::Install)
Provides:       perl(ExtUtils::MM)
Provides:       perl(ExtUtils::MM::Utils)
Provides:       perl(ExtUtils::ParseXS)
Provides:       perl(File::Compare)
Provides:       perl(File::stat)
Provides:       perl(FileHandle)
Provides:       perl(Hash::Util::FieldHash)
Provides:       perl(I18N::LangTags)
Provides:       perl(I18N::LangTags::Detect)
Provides:       perl(I18N::Langinfo)
Provides:       perl(IO::Dir)
Provides:       perl(IO::Pipe)
Provides:       perl(IO::Poll)
Provides:       perl(IO::Socket::INET)
Provides:       perl(IO::Socket::UNIX)
Provides:       perl(Math::Complex)
Provides:       perl(Math::Trig)
Provides:       perl(O)
Provides:       perl(Opcode)
Provides:       perl(PerlIO)
Provides:       perl(PerlIO::encoding)
Provides:       perl(Safe)
Provides:       perl(Search::Dict)
Provides:       perl(Term::ReadLine)
Provides:       perl(Test::Builder::Module)
Provides:       perl(Text::Abbrev)
Provides:       perl(Thread::Semaphore)
Provides:       perl(Tie::ExtraHash)
Provides:       perl(Tie::File)
Provides:       perl(autouse)
Provides:       perl(encoding)
Provides:       perl(B)
Provides:       perl(B::Deparse)
Provides:       perl(Carp)
Provides:       perl(Config)
Provides:       perl(Cwd)
Provides:       perl(Data::Dumper)
Provides:       perl(Digest::MD5)
Provides:       perl(Digest::SHA)
Provides:       perl(DynaLoader)
Provides:       perl(Encode)
Provides:       perl(Encode::Alias)
Provides:       perl(Errno)
Provides:       perl(Exporter)
Provides:       perl(ExtUtils::MakeMaker)
Provides:       perl(ExtUtils::Manifest)
Provides:       perl(Fcntl)
Provides:       perl(File::Basename)
Provides:       perl(File::Copy)
Provides:       perl(File::Find)
Provides:       perl(File::Glob)
Provides:       perl(File::Path)
Provides:       perl(File::Spec)
Provides:       perl(File::Temp)
Provides:       perl(FindBin)
Provides:       perl(Getopt::Long)
Provides:       perl(Getopt::Std)
Provides:       perl(Hash::Util)
Provides:       perl(IO)
Provides:       perl(IO::File)
Provides:       perl(IO::Handle)
Provides:       perl(IO::Seekable)
Provides:       perl(IO::Select)
Provides:       perl(IO::Socket)
Provides:       perl(IPC::Cmd)
Provides:       perl(IPC::Open2)
Provides:       perl(IPC::Open3)
Provides:       perl(JSON::PP)
Provides:       perl(List::Util)
Provides:       perl(MIME::Base64)
Provides:       perl(MIME::QuotedPrint)
Provides:       perl(POSIX)
Provides:       perl(Scalar::Util)
Provides:       perl(SelectSaver)
Provides:       perl(Socket)
Provides:       perl(Storable)
Provides:       perl(Symbol)
Provides:       perl(Sys::Hostname)
Provides:       perl(Text::ParseWords)
Provides:       perl(Text::Tabs)
Provides:       perl(Text::Wrap)
Provides:       perl(Thread::Queue)
Provides:       perl(Time::HiRes)
Provides:       perl(Time::Local)
Provides:       perl(Unicode::Normalize)
Provides:       perl(XSLoader)
Provides:       perl(blib)
Provides:       perl(bytes)
Provides:       perl(constant)
Provides:       perl(diagnostics)
Provides:       perl(experimental)
Provides:       perl(feature)
Provides:       perl(if)
Provides:       perl(integer)
Provides:       perl(lib)
Provides:       perl(locale)
Provides:       perl(mro)
Provides:       perl(ok)
Provides:       perl(open)
Provides:       perl(overload)
Provides:       perl(parent)
Provides:       perl(re)
Provides:       perl(strict)
Provides:       perl(threads)
Provides:       perl(threads::shared)
Provides:       perl(utf8)
Provides:       perl(vars)
Provides:       perl(version)
Provides:       perl(warnings)
Provides:       perl(NEXT)
Provides:       perl(SelfLoader)
Provides:       perl(List::Util::XS)
# oreon:deps
BuildRequires:  bash
BuildRequires:  bzip2-devel
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
BuildRequires:  glibc-common
BuildRequires:  glibc-langpack-tr
BuildRequires:  groff-base
BuildRequires:  libdb-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  procps
BuildRequires:  sed
BuildRequires:  systemtap-sdt-devel
BuildRequires:  systemtap-sdt-dtrace
BuildRequires:  tar
BuildRequires:  zlib-devel
# /oreon:deps
%description
Perl is a high-level programming language with roots in C, sed, awk and shell
scripting. Perl is good at handling processes and files, and is especially
good at handling text. Perl's hallmarks are practicality and efficiency.
While it is used to do a lot of different things, Perl's most common
applications are system administration utilities and web programming.

This is a metapackage with all the Perl bits and core modules that can be
found in the upstream tarball from perl.org.

If you need only a specific feature, you can install a specific package
instead. E.g. to handle Perl scripts with %{_bindir}/perl interpreter,
install perl-interpreter package. See perl-interpreter description for more
details on the Perl decomposition into packages.

%package interpreter
Summary:        Standalone executable Perl interpreter
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Version:        %{perl_version}
Epoch:          %{perl_epoch}
Requires:       perl-libs%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Suggests:       perl-doc = %{perl_version}-%{release}
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_interpreter
%endif
Requires(post): perl-libs
Obsoletes:      perl-suidperl <= 4:5.12.2
Obsoletes:      perl < 4:5.26.0-395
%description interpreter
This is a Perl interpreter as a standalone executable %{_bindir}/perl
required for handling Perl scripts. It does not provide all the other Perl
modules or tools.

Install this package if you want to program in Perl or enable your system to
handle Perl scripts with %{_bindir}/perl interpreter.

If your script requires some Perl modules, you can install them with
"perl(MODULE)" where "MODULE" is a name of required module. E.g. install
"perl(Test::More)" to make Test::More Perl module available.

If you need all the Perl modules that come with upstream Perl sources, so
called core modules, install perl package.

If you only need perl run-time as a shared library, i.e. Perl interpreter
embedded into another application, the only essential package is perl-libs.

Perl header files can be found in perl-devel package.

Perl utils like "h2ph" or "perlbug" can be found in perl-utils package.

Perl debugger, usually invoked with "perl -d", is available in perl-debugger
package.

%package libs
Summary:        The libraries for the perl run-time
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Martin-Birgmeier AND Spencer-86 AND MIT AND Unicode-3.0 AND LicenseRef-Fedora-Public-Domain
Provides:       %perl_compat
Provides:       perl(:MODULE_COMPAT_5.42.1)
Provides:       perl(:MODULE_COMPAT_5.42.0)
Provides:       perl(:VERSION) = %{perl_version}
Provides:       perl(:WITH_64BIT)
Provides:       perl(:WITH_ITHREADS)
Provides:       perl(:WITH_THREADS)
Provides:       perl(:WITH_LARGEFILES)
Provides:       perl(:WITH_PERLIO)
Provides:       perl(unicore::Name)
Provides:       perl(utf8_heavy.pl)
%if %{with bdb}
Suggests:       perl(DB_File)
%endif
Requires:       perl(DynaLoader)
Requires:       perl(Encode)
Requires:       perl(File::Spec)
%if %{with gdbm}
Suggests:       perl(GDBM_File)
Recommends:     perl(NDBM_File)
Suggests:       perl(ODBM_File)
%endif
%if %{defined perl_bootstrap}
%gendep_perl_libs
%endif
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\((charnames|DynaLoader)\\)$
%description libs
The is a perl run-time (interpreter as a shared library and include
directories).

%package devel
Summary:        Header files for use in perl development
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Unicode-3.0
%if %{with perl_enables_systemtap}
Requires:       systemtap-sdt-devel
Requires:       systemtap-sdt-dtrace
%endif
Requires:       perl(ExtUtils::ParseXS)
Requires:       perl-libs%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Recommends:     perl-doc = %{perl_version}-%{release}
Requires:       perl(Devel::PPPort)
Requires:       redhat-rpm-config
Requires:       libxcrypt-devel%{?_isa}
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_devel
%endif
%description devel
This package contains header files and development modules.
Most perl packages will need to install perl-devel to build.

%package macros
Summary:        Macros for rpmbuild
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
Requires:       perl-interpreter
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_macros
%endif
%description macros
RPM macros that are handy when building binary RPM packages.

%package tests
Summary:        The Perl test suite
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
AutoReqProv:    0
Requires:       perl
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_tests
%endif
%description tests
This package contains the test suite included with Perl %{perl_version}.

Install this if you want to test your Perl installation (binary and core
modules).

%package utils
Summary:        Utilities packaged with the Perl distribution
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        %{perl_version}
BuildArch:      noarch
Requires:       perl-libs = %{perl_epoch}:%{perl_version}-%{release}
%if %{defined perl_bootstrap}
%gendep_perl_utils
%endif
Conflicts:      perl < 4:5.22.0-351
%description utils
Several utilities which come with Perl distribution like h2ph, perlbug,
perlthanks, and pl2pm. Some utilities are provided by more specific
packages like perldoc by perl-Pod-Perldoc and splain by perl-diagnostics.

%if %{dual_life} || %{rebuild_from_scratch}
%package Archive-Tar
Summary:        A module for Perl manipulation of .tar files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        3.04
BuildArch:      noarch
Requires:       perl(IO::Zlib) >= 1.01
Requires:       perl(IO::Compress::Bzip2) >= 2.015
Requires:       perl(IO::Uncompress::Bunzip2) >= 2.015
%if !%{defined perl_bootstrap}
Requires:       perl(Text::Diff)
%endif
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Archive_Tar
%endif
%description Archive-Tar
Archive::Tar provides an object oriented mechanism for handling tar files.  It
provides class methods for quick and easy files handling while also allowing
for the creation of tar file objects for custom manipulation.  If you have the
IO::Zlib module installed, Archive::Tar will also support compressed or
gzipped tar files.
%endif

%package Attribute-Handlers
Summary:        Simpler definition of attribute handlers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.03
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Attribute_Handlers
%endif
Conflicts:      perl < 4:5.22.0-351
%description Attribute-Handlers
This Perl module, when inherited by a package, allows that package's class to
define attribute handler subroutines for specific attributes. Variables and
subroutines subsequently defined in that package, or in packages derived from
that package may be given attributes with the same names as the attribute
handler subroutines, which will then be called in one of the compilation
phases (i.e. in a "BEGIN", "CHECK", "INIT", or "END" block).

%if %{dual_life} || %{rebuild_from_scratch}
%package autodie
Summary:        Replace functions with ones that succeed or die
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.37
BuildArch:      noarch
Requires:       perl(B)
Requires:       perl(Fcntl)
Requires:       perl(overload)
Requires:       perl(POSIX)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_autodie
%endif
Conflicts:      perl < 4:5.16.2-259
%description autodie
The "autodie" and "Fatal" pragma provides a convenient way to replace
functions that normally return false on failure with equivalents that throw an
exception on failure.

However "Fatal" has been obsoleted by the new autodie pragma. Please use
autodie in preference to "Fatal".
%endif

%package AutoLoader
Summary:        Load subroutines only on demand
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        5.74
BuildArch:      noarch
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_AutoLoader
%endif
Conflicts:      perl < 4:5.30.1-451
%description AutoLoader
The AutoLoader module works with the AutoSplit module and the "__END__" token
to defer the loading of some subroutines until they are used rather than
loading them all at once.

%package AutoSplit
Summary:        Split a package for automatic loading
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        5.74
BuildArch:      noarch
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_AutoSplit
%endif
Conflicts:      perl < 4:5.30.1-451
%description AutoSplit
Split up your program into files that the AutoLoader module can handle. It is
used by both the standard Perl libraries and by the ExtUtils::MakeMaker
utility, to automatically configure libraries for automatic loading.

%package autouse
Summary:        Postpone load of modules until a function is used
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.11
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(warnings)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_autouse
%endif
Conflicts:      perl < 4:5.30.1-451
%description autouse
If a module is not loaded yet, then the autouse declaration declares functions
in the current package. When these functions are called, they load the package
and substitute themselves with the correct definitions.

%package B
Summary:        Perl compiler backend
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.89
Requires:       perl(Data::Dumper)
Requires:       perl(overloading)
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_B
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description B
The "B" module supplies classes which allow a Perl program to delve into its
own innards. It is the module used to implement the backends of the Perl
compiler.

%package base
Summary:        Establish an ISA relationship with base classes at compile time
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.27
BuildArch:      noarch
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_base
%endif
Conflicts:      perl < 4:5.30.1-451
%description base
"base" module allows you to both load one or more modules, while setting up
inheritance from those modules at the same time.  Unless you are using the
"fields" pragma, consider this module discouraged in favor of the
lighter-weight "parent".

%package Benchmark
Summary:        Benchmark running times of Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.27
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Benchmark
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Benchmark
The Benchmark module encapsulates a number of routines to help you figure out
how long it takes to execute some code.

%if %{dual_life} || %{rebuild_from_scratch}
%package bignum
Summary:        Transparent big number support for Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.67
Requires:       perl(Carp)
Requires:       perl(Math::BigRat)
Requires:       perl(warnings)
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_bignum
%endif
Conflicts:      perl < 4:5.22.0-348
%description bignum
This package attempts to make it easier to write scripts that use BigInts and
BigFloats in a transparent way.
%endif

%package blib
Summary:        Use uninstalled version of a package
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.07
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_blib
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description blib
This module looks for MakeMaker-like "blib" directory structure starting in
given or current directory and working back up to five levels of directories.
It is intended for use on command line with -M option as a way of testing
arbitrary scripts against an uninstalled version of a package.

%if %{dual_life} || %{rebuild_from_scratch}
%package Carp
Summary:        Alternative warn and die for modules
Epoch:          0
Version:        1.54
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Carp
%endif
BuildArch:      noarch
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Carp\\)\\s*$
%description Carp
The Carp routines are useful in your own modules because they act like
die() or warn(), but with a message which is more likely to be useful to a
user of your module. In the case of cluck, confess, and longmess that
context is a summary of every call in the call-stack. For a shorter message
you can use carp or croak which report the error as being from where your
module was called. There is no guarantee that that is where the error was,
but it is a good educated guess.
%endif

%package Class-Struct
Summary:        Declare struct-like data types as Perl classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.68
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Class_Struct
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Class-Struct
Class::Struct module exports a single function struct(). Given a list of
element names and types, and optionally a class name, struct() creates a
Perl 5 class that implements a struct-like data structure.

%if %{dual_life} || %{rebuild_from_scratch}
%package Compress-Raw-Bzip2
Summary:        Low-Level Interface to bzip2 compression library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.213
Requires:       perl(Exporter), perl(File::Temp)
%if %{defined perl_bootstrap}
%gendep_perl_Compress_Raw_Bzip2
%endif
%description Compress-Raw-Bzip2
This module provides a Perl interface to the bzip2 compression library.
It is used by IO::Compress::Bzip2.

%package Compress-Raw-Zlib
Summary:        Low-Level Interface to the zlib compression library
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Zlib
Epoch:          0
Version:        2.213
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Compress_Raw_Zlib
%endif
%description Compress-Raw-Zlib
This module provides a Perl interface to the zlib compression library.
It is used by IO::Compress::Zlib.
%endif

%package Config-Extensions
Summary:        Hash lookup of which Perl core extensions were built
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.03
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Config_Extensions
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Config-Extensions
The Config::Extensions module provides a hash %%Extensions containing all the
core extensions that were enabled for this perl.

%if %{dual_life} || %{rebuild_from_scratch}
%package Config-Perl-V
Summary:        Structured data retrieval of perl -V output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.38
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Config_Perl_V
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347
%description Config-Perl-V
The command "perl -V" will return you an excerpt from the %%Config::Config
hash combined with the output of "perl -V" that is not stored inside the hash,
but only available to the perl binary itself. This package provides Perl
module that will return you the output of "perl -V" in a structure.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package constant
Summary:        Perl pragma to declare constants
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.33
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_constant
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.3-264
%description constant
This pragma allows you to declare constants at compile-time:

use constant PI => 4 * atan2(1, 1);

When you declare a constant such as "PI" using the method shown above,
each machine your script runs upon can have as many digits of accuracy
as it can use. Also, your program will be easier to read, more likely
to be maintained (and maintained correctly), and far less likely to
send a space probe to the wrong planet because nobody noticed the one
equation in which you wrote 3.14195.

When a constant is used in an expression, Perl replaces it with its
value at compile time, and may then optimize the expression further.
In particular, any code in an "if (CONSTANT)" block will be optimized
away if the constant is false.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package CPAN
Summary:        Query, download and build perl modules from CPAN sites
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.38
Requires:       make
Requires:       perl
Requires:       perl(Archive::Tar) >= 1.50
Requires:       perl(base)
Requires:       perl(Data::Dumper)
%if !%{defined perl_bootstrap}
Requires:       perl(Devel::Size)
%endif
Requires:       perl(ExtUtils::Manifest)
%if !%{defined perl_bootstrap}
Requires:       perl(File::HomeDir) >= 0.65
%endif
Requires:       perl(File::Temp) >= 0.16
Requires:       perl(lib)
Requires:       perl(Net::Config)
Requires:       perl(Net::FTP)
Requires:       perl(POSIX)
Requires:       perl(Term::ReadLine)
%if !%{defined perl_bootstrap}
Requires:       perl(URI)
Requires:       perl(URI::Escape)
%endif
Requires:       perl(User::pwent)
%if !%{defined perl_bootstrap}
Requires:       perl(Archive::Zip)
Requires:       perl(Compress::Bzip2)
Requires:       perl(CPAN::Meta) >= 2.110350
%endif
Requires:       perl(Compress::Zlib)
Requires:       perl(Digest::MD5)
Requires:       perl(Digest::SHA)
Requires:       perl(Dumpvalue)
Requires:       perl(ExtUtils::CBuilder)
%if ! %{defined perl_bootstrap}
Requires:       perl(local::lib)
%endif
Requires:       perl(Module::Build)
%if ! %{defined perl_bootstrap}
Requires:       perl(Text::Glob)
%endif
Provides:       cpan = %{version}
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_CPAN
%endif
BuildArch:      noarch
%description CPAN
The CPAN module automates or at least simplifies the make and install of
perl modules and extensions. It includes some primitive searching
capabilities and knows how to use LWP, HTTP::Tiny, Net::FTP and certain
external download clients to fetch distributions from the net.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package CPAN-Meta
Summary:        Distribution metadata for a CPAN dist
Epoch:          0
Version:        2.150010
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       perl(CPAN::Meta::YAML) >= 0.011
Requires:       perl(Encode)
Requires:       perl(JSON::PP) >= 2.27300
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_CPAN_Meta
%endif
BuildArch:      noarch
%description CPAN-Meta
Software distributions released to the CPAN include a META.json or, for
older distributions, META.yml, which describes the distribution, its
contents, and the requirements for building and installing the
distribution. The data structure stored in the META.json file is described
in CPAN::Meta::Spec.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package CPAN-Meta-Requirements
Summary:        Set of version requirements for a CPAN dist
Epoch:          0
Version:        2.143
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(CPAN::Meta::Requirements\\)
Provides:       perl(CPAN::Meta::Requirements) = %{version}000
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_CPAN_Meta_Requirements
%endif
%description CPAN-Meta-Requirements
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions.
It can be built up by adding more and more constraints, and it will reduce
them to the simplest representation.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package CPAN-Meta-YAML
Version:        0.020
Epoch:          0
Summary:        Read and write a subset of YAML for CPAN Meta files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_CPAN_Meta_YAML
%endif
%description CPAN-Meta-YAML
This module implements a subset of the YAML specification for use in reading
and writing CPAN metadata files like META.yml and MYMETA.yml. It should not be
used for any other general YAML parsing or generation task.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Data-Dumper
Summary:        Stringify perl data structures, suitable for printing and eval
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.192
Requires:       perl(B::Deparse)
Requires:       perl(bytes)
Requires:       perl(Scalar::Util)
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Data_Dumper
%endif
%description Data-Dumper
Given a list of scalars or reference variables, writes out their contents
in perl syntax. The references can also be objects. The content of each
variable is output in a single Perl statement. Handles self-referential
structures correctly.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%if %{with bdb}
%package DB_File
Summary:        Perl5 access to Berkeley DB version 1.x
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.859
Requires:       perl(Fcntl)
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_DB_File
%endif
Conflicts:      perl < 4:5.16.3-264
%description DB_File
DB_File is a module which allows Perl programs to make use of the facilities
provided by Berkeley DB version 1.x (if you have a newer version of DB, you
will be limited to functionality provided by interface of version 1.x). The
interface defined here mirrors the Berkeley DB interface closely.
%endif
%endif

%package DBM_Filter
Summary:        Filter DBM keys and values
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.07
Requires:       perl(Compress::Zlib)
Requires:       perl(Encode)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_DBM_Filter
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Tie::Hash\\)$
%description DBM_Filter
This module provides an interface that allows filters to be applied to tied
hashes associated with DBM files.

%package debugger
Summary:        Perl debugger
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.60
BuildArch:      noarch
Provides:       perl(dumpvar.pl) = %{perl_version}
Provides:       perl(perl5db.pl) = %{version}
Recommends:     perl(Carp)
Recommends:     perl(Config)
Requires:       perl(Cwd)
Recommends:     perl(Devel::Peek)
Requires:       perl(feature)
Recommends:     perl(IO::Handle)
Recommends:     perl(File::Basename)
Recommends:     perl(File::Path)
Requires:       perl(IO::Socket)
Requires:       perl(meta_notation) = %{perl_version}
Requires:       perl(mro)
%if !%{defined perl_bootstrap}
Suggests:       perl(PadWalker) >= 0.08
%endif
Recommends:     perl(POSIX)
Requires:       perl(Term::ReadLine)
Requires:       perl(threads)
Requires:       perl(threads::shared)
Requires:       perl(vars)
Requires:       perl(warnings)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_debugger
%endif
Conflicts:      perl < 4:5.30.1-451
%description debugger
This is the perl debugger. It is loaded automatically by Perl when you invoke
a script with "perl -d". There is also "DB" module contained for
a programmatic interface to the debugging API.

%package deprecate
Summary:        Perl pragma for deprecating the inclusion of a module in core
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.04
Requires:       perl(Carp)
Requires:       perl(Config)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_deprecate
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description deprecate
"deprecate" pragma simplifies the maintenance of dual-life modules that will no
longer be included in the Perl core in a future Perl release, but are
still included currently. The purpose of the pragma is to alert users to the
status of such a module by issuing a warning that encourages them to install
the module from CPAN, so that a future upgrade to a perl which omits the
module will not break their code.

%package Devel-Peek
Summary:        A data debugging tool for the XS programmer
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.36
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Devel_Peek
%endif
Conflicts:      perl < 4:5.22.0-351
%description Devel-Peek
Devel::Peek contains functions which allows raw Perl data types to be
manipulated from a Perl script. This is used by those who do XS programming to
check that the data they are sending from C to Perl looks as they think it
should look.

%if %{dual_life} || %{rebuild_from_scratch}
%package Devel-PPPort
Summary:        Perl Pollution Portability header generator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        3.73
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Devel_PPPort
%endif
Conflicts:      perl < 4:5.20.1-310
%description Devel-PPPort
Perl's API has changed over time, gaining new features, new functions,
increasing its flexibility, and reducing the impact on the C name space
environment (reduced pollution). The header file written by this module,
typically ppport.h, attempts to bring some of the newer Perl API features
to older versions of Perl, so that you can worry less about keeping track
of old releases, but users can still reap the benefit.
%endif

%package Devel-SelfStubber
Summary:        Generate stubs for a SelfLoading module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.06
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Devel_SelfStubber
%endif
Conflicts:      perl < 4:5.22.0-351
%description Devel-SelfStubber
Devel::SelfStubber prints the stubs you need to put in the module before the
__DATA__ token (or you can get it to print the entire module with stubs
correctly placed). The stubs ensure that if a method is called, it will get
loaded. They are needed specifically for inherited autoloaded methods.

%package diagnostics
Summary:        Produce verbose warning diagnostics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.40
BuildArch:      noarch
Requires:       perl-libs = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Getopt::Std)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_diagnostics
%endif
Conflicts:      perl-utils < 5.30.1-451
Conflicts:      perl-interpreter < 4:5.30.1-451
%description diagnostics
The diagnostics module extends the terse diagnostics normally emitted by both
the perl compiler and the perl interpreter (from running perl with a -w switch
or "use warnings"), augmenting them with the more explicative and endearing
descriptions found in perldiag. splain tool explains perl messages found on
standard input.

%if %{dual_life} || %{rebuild_from_scratch}
%package Digest
Summary:        Modules that calculate message digests
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.20
BuildArch:      noarch
Requires:       perl(MIME::Base64)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Digest
%endif
%description Digest
The Digest:: modules calculate digests, also called "fingerprints" or
"hashes", of some data, called a message. The digest is (usually)
some small/fixed size string. The actual size of the digest depend of
the algorithm used. The message is simply a sequence of arbitrary
bytes or bits.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Digest-MD5
Summary:        Perl interface to the MD5 Algorithm
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.59
Requires:       perl(XSLoader)
Requires:       perl(Digest::base) >= 1.00
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Digest_MD5
%endif
%description Digest-MD5
The Digest::MD5 module allows you to use the RSA Data Security Inc. MD5
Message Digest algorithm from within Perl programs. The algorithm takes as
input a message of arbitrary length and produces as output a 128-bit
"fingerprint" or "message digest" of the input.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Digest-SHA
Summary:        Perl extension for SHA-1/224/256/384/512
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        6.04
Requires:       perl(Carp)
Requires:       perl(Digest::base)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Digest_SHA
%endif
%description Digest-SHA
Digest::SHA is a complete implementation of the NIST Secure Hash
Standard.  It gives Perl programmers a convenient way to calculate
SHA-1, SHA-224, SHA-256, SHA-384, and SHA-512 message digests.  The
module can handle all types of input, including partial-byte data.
%endif

%package DirHandle
Summary:        Supply object methods for directory handles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.05
BuildArch:      noarch
Requires:       perl(warnings)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_DirHandle
%endif
Conflicts:      perl < 4:5.30.1-451
%description DirHandle
There is no reason to use this module nowadays. The DirHandle module provides
an alternative interface to the opendir(), closedir(), readdir(), and
rewinddir() functions. Since Perl 5.6, opendir() alone has been all you need
for lexical handles.

%package doc
Summary:        Perl language documentation
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Unicode-3.0 AND LicenseRef-Fedora-UltraPermissive
Epoch:          0
Version:        %{perl_version}
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%endif
Recommends:     perl-Pod-Perldoc
Conflicts:      perl < 4:5.30.1-451
%description doc
This is a documentation for Perl language. It's provided in POD and manual
page format.

%package Dumpvalue
Summary:        Screen dump of Perl data
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.27
BuildArch:      noarch
Recommends:     perl(Devel::Peek)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Dumpvalue
%endif
Conflicts:      perl < 4:5.30.1-451
%description Dumpvalue
Dumpvalue module enables you to print a content of variables and other Perl
data structures.

%package DynaLoader
Summary:        Dynamically load C libraries into Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.57
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_DynaLoader
%endif
Conflicts:      perl < 4:5.30.1-451
%description DynaLoader
The DynaLoader module defines a standard generic interface to the dynamic
linking mechanisms available on many platforms. Its primary purpose is to
implement automatic dynamic loading of Perl modules. For a simpler interface,
see XSLoader module.

%if %{dual_life} || %{rebuild_from_scratch}
%package Encode
Summary:        Character encodings in Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Artistic-2.0
Epoch:          4
Version:        3.21
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Encode
%endif
Conflicts:      perl < 4:5.16.2-256
%description Encode
The Encode module provides the interface between Perl strings and the rest
of the system. Perl strings are sequences of characters.

%package encoding
Summary:        Write your Perl script in non-ASCII or non-UTF-8
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          4
Version:        3.00
Requires:       perl(Carp)
Requires:       perl(Filter::Util::Call)
Requires:       perl(utf8)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_encoding
%endif
Conflicts:      perl-Encode < 2:2.60-314
%description encoding
With the encoding pragma, you can write your Perl script in any encoding you
like (so long as the Encode module supports it) and still enjoy Unicode
support.

However, this encoding module is deprecated under perl 5.18. It uses
a mechanism provided by perl that is deprecated under 5.18 and higher, and may
be removed in a future version.GPL-1.0-or-later OR Artistic-1.0-Perl

The easiest and the best alternative is to write your script in UTF-8.

%package Encode-devel
Summary:        Character encodings in Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          4
Version:        3.21
Requires:       %{name}-Encode = %{epoch}:%{version}-%{release}
Recommends:     perl-devel
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Encode_devel
%endif
BuildArch:      noarch
%description Encode-devel
enc2xs builds a Perl extension for use by Encode from either Unicode Character
Mapping files (.ucm) or Tcl Encoding Files (.enc). You can use enc2xs to add
your own encoding to perl. No knowledge of XS is necessary.
%endif

%package encoding-warnings
Summary:        Warn on implicit encoding conversions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.14
BuildArch:      noarch
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_encoding_warnings
%endif
Conflicts:      perl < 4:5.30.1-451
%description encoding-warnings
As of Perl 5.26.0, this module has no effect. The internal Perl feature that
was used to implement this module has been removed.  Hence, if you load this
module on Perl 5.26.0, you will get one warning that the module is no longer
supported; and the module will do nothing thereafter.

%package English
Summary:        Nice English or awk names for ugly punctuation variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.11
Requires:       perl(Carp)
Requires:       perl(warnings)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_English
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description English
This module provides aliases for the built-in variables whose names no one
seems to like to read.

%if %{dual_life} || %{rebuild_from_scratch}
%package Env
Summary:        Perl module that imports environment variables as scalars or arrays
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.06
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Env
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-265
%description Env
Perl maintains environment variables in a special hash named %%ENV. For when
this access method is inconvenient, the Perl module Env allows environment
variables to be treated as scalar or array variables.
%endif

%package Errno
Summary:        System errno constants
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.38
Requires:       perl-libs%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Errno
%endif
Conflicts:      perl < 4:5.22.0-351
%description Errno
"Errno" defines and conditionally exports all the error constants defined in
your system "errno.h" include file. It has a single export tag, ":POSIX",
which will export all POSIX defined error numbers.

%if %{dual_life} || %{rebuild_from_scratch}
%package experimental
Summary:        Experimental features made easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.035
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_experimental
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.20.0-303
%description experimental
This pragma provides an easy and convenient way to enable or disable
experimental features.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Exporter
Summary:        Implements default import method for modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        5.79
Requires:       perl(Carp) >= 1.05
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Exporter
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-265
%description Exporter
The Exporter module implements an import method which allows a module to
export functions and variables to its users' name spaces. Many modules use
Exporter rather than implementing their own import method because Exporter
provides a highly flexible interface, with an implementation optimized for
the common case.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-CBuilder
Summary:        Compile and link C code for Perl modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        0.280242
BuildArch:      noarch
Requires:       gcc
Requires:       gcc-c++
Requires:       perl-devel
Requires:       perl(DynaLoader)
Requires:       perl(ExtUtils::Mksymlists)
Requires:       perl(File::Spec) >= 3.13
Requires:       perl(Perl::OSType) >= 1
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_CBuilder
%endif
%description ExtUtils-CBuilder
This module can build the C portions of Perl modules by invoking the
appropriate compilers and linkers in a cross-platform manner. It was motivated
by the Module::Build project, but may be useful for other purposes as well.
%endif

%package ExtUtils-Constant
Summary:        Generate XS code to import C header constants
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.25
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Conflicts:      perl-interpreter < 4:5.30.1-451
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_Constant
%endif
%description ExtUtils-Constant
ExtUtils::Constant facilitates generating C and XS wrapper code to allow
Perl modules to AUTOLOAD constants defined in C library header files.

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-Command
Summary:        Perl routines to replace common UNIX commands in Makefiles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          2
Version:        7.76
BuildArch:      noarch
Conflicts:      perl < 4:5.20.1-312
Requires:       perl(File::Find)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_Command
%endif
%description ExtUtils-Command
This Perl module is used to replace common UNIX commands. In all cases the
functions work with @ARGV rather than taking arguments. This makes them
easier to deal with in Makefiles.
%endif

%package ExtUtils-Embed
Summary:        Utilities for embedding Perl in C/C++ applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.35
Requires:       perl-devel
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_Embed
%endif
BuildArch:      noarch
%description ExtUtils-Embed
Utilities for embedding Perl in C/C++ applications.

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-Install
Summary:        Install files from here to there
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.22
BuildArch:      noarch
Requires:       perl(AutoSplit)
Requires:       perl(File::Compare)
Requires:       perl(Data::Dumper)
Recommends:     perl(POSIX)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_Install
%endif
%description ExtUtils-Install
Handles the installing and uninstalling of perl modules, scripts, man
pages, etc.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-MakeMaker
Summary:        Create a module Makefile
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          2
Version:        7.76
Recommends:     gcc
Recommends:     perl-devel
Requires:       perl(Data::Dumper)
Requires:       perl(DynaLoader)
Requires:       perl(ExtUtils::Command)
Requires:       perl(ExtUtils::Install)
Requires:       perl(ExtUtils::Manifest)
Requires:       perl(File::Find)
Requires:       perl(Getopt::Long)
Requires:       perl(Pod::Man)
Requires:       perl(POSIX)
Requires:       perl(Test::Harness)
Requires:       perl(version)
Requires:       perl-ExtUtils-ParseXS
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_MakeMaker
%endif
BuildArch:      noarch
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DynaLoader\\)\\s*$
%global __provides_exclude %__provides_exclude|^perl\\(ExtUtils::MakeMaker::_version\\)
%description ExtUtils-MakeMaker
Create a module Makefile.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-Manifest
Summary:        Utilities to write and check a MANIFEST file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        1.75
Requires:       perl(File::Path)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_Manifest
%endif
BuildArch:      noarch
%description ExtUtils-Manifest
%{summary}.
%endif

%package ExtUtils-Miniperl
Summary:        Write the C code for perlmain.c
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.14
Requires:       perl-devel
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_Miniperl
%endif
BuildArch:      noarch
%description ExtUtils-Miniperl
writemain() takes an argument list of directories containing archive libraries
that relate to perl modules and should be linked into a new perl binary. It
writes a corresponding perlmain.c file that is a plain C file containing all
the bootstrap code to make the If the first argument to writemain() is a
reference to a scalar it is used as the file name to open for output. Any other
reference is used as the file handle to write to. Otherwise output defaults to
STDOUT.

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-MM-Utils
Summary:        ExtUtils::MM methods without dependency on ExtUtils::MakeMaker
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        7.44
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_MM_Utils
%endif
%description ExtUtils-MM-Utils
This is a collection of ExtUtils::MM subroutines that are used by many
other modules but that do not need full-featured ExtUtils::MakeMaker. The
issue with ExtUtils::MakeMaker is it pulls in Perl header files and that
is an overkill for small subroutines.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package ExtUtils-ParseXS
Summary:        Module and a script for converting Perl XS code into C code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        3.57
Requires:       perl(fields)
Requires:       perl(Hash::Util)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ExtUtils_ParseXS
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
BuildArch:      noarch
%description ExtUtils-ParseXS
ExtUtils::ParseXS will compile XS code into C code by embedding the constructs
necessary to let C functions manipulate Perl values and creates the glue
necessary to let Perl access those functions.
%endif

%package Fcntl
Summary:        File operation options
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.20
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Fcntl
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Fcntl
Fcntl module provides file operation related options.

%package fields
Summary:        Compile-time class fields
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.27
BuildArch:      noarch
Requires:       perl(base)
Requires:       perl(Carp)
Requires:       perl(Hash::Util)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_fields
%endif
Conflicts:      perl < 4:5.30.1-451
%description fields
The "fields" pragma enables compile-time and run-time verified class fields.

%package File-Basename
Summary:        Parse file paths into directory, file name, and suffix
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.86
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(re)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_File_Basename
%endif
Conflicts:      perl < 4:5.30.1-451
%description File-Basename
These routines allow you to parse file paths into their directory, file name,
and suffix.

%package File-Compare
Summary:        Compare files or file handles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.100.800
BuildArch:      noarch
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_File_Compare
%endif
Conflicts:      perl < 4:5.30.1-451
%description File-Compare
A File::Compare Perl module provides functions for comparing a content of two
files specified by a file name or a file handle.

%package File-Copy
Summary:        Copy files or file handles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.41
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(File::Basename)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_File_Copy
%endif
Conflicts:      perl < 4:5.30.1-451
%description File-Copy
A File::Copy module provides two basic functions, copy and move, which are
useful for getting the contents of a file from one place to another.

%package File-DosGlob
Summary:        DOS-like globbing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.12
Requires:       perl(Text::ParseWords)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_File_DosGlob
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description File-DosGlob
This Perl module implements DOS-like globbing with a few enhancements. It
is largely compatible with perlglob.exe in all but one respect--it understands
wild cards in directory components.

%if %{dual_life} || %{rebuild_from_scratch}
%package File-Fetch
Summary:        Generic file fetching mechanism
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.04
Requires:       perl(IPC::Cmd) >= 0.36
Requires:       perl(Module::Load::Conditional) >= 0.04
Requires:       perl(Params::Check) >= 0.07
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_File_Fetch
%endif
BuildArch:      noarch
%description File-Fetch
File::Fetch is a generic file fetching mechanism.
%endif

%package File-Find
Summary:        Traverse a directory tree
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.44
Recommends:     perl(Scalar::Util)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_File_Find
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description File-Find
These are functions for searching through directory trees doing work on each
file found similar to the Unix find command.

%if %{dual_life} || %{rebuild_from_scratch}
%package File-Path
Summary:        Create or remove directory trees
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.18
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_File_Path
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-265
%description File-Path
This module provides a convenient way to create directories of arbitrary
depth and to delete an entire directory subtree from the file system.
%endif

%package File-stat
Summary:        By-name interface to Perl built-in stat functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.14
BuildArch:      noarch
Requires:       perl(Symbol)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_File_stat
%endif
Conflicts:      perl < 4:5.30.1-451
%description File-stat
This module overrides the core stat() and lstat() functions, replacing them
with versions that return File::stat objects. This object has methods that
return the similarly named structure field name from the stat(2) function.

%if %{dual_life} || %{rebuild_from_scratch}
%package File-Temp
Summary:        Return name and handle of a temporary file safely
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        0.231.100
BuildArch:      noarch
Requires:       perl(File::Path) >= 2.06
Requires:       perl(POSIX)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_File_Temp
%endif
Conflicts:      perl < 4:5.16.2-265
%description File-Temp
File::Temp can be used to create and open temporary files in a safe way.
There is both a function interface and an object-oriented interface. The
File::Temp constructor or the tempfile() function can be used to return the
name and the open file handle of a temporary file. The tempdir() function
can be used to create a temporary directory.
%endif

%package FileCache
Summary:        Keep more files open than the system permits
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.10
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_FileCache
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description FileCache
The "cacheout" function will make sure that there's a file handle open
for reading or writing available as the path name you give it. It
automatically closes and re-opens files if you exceed your system
maximum number of file descriptors, or the suggested maximum.

%package FileHandle
Summary:        Object methods for file handles
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.05
BuildArch:      noarch
Requires:       perl(Exporter)
Recommends:     perl(Fcntl)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_FileHandle
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description FileHandle
This is an object-oriented interface for opening files and performing
input/output operations on them.

%package filetest
Summary:        Perl pragma to control the filetest permission operators
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.03
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_filetest
%endif
Conflicts:      perl < 4:5.30.1-451
%description filetest
The default behavior of file test operators (e.g. "-r") is to use the simple
mode bits as returned by the stat() family of system calls. However, many
operating systems have additional features to define more complex access
rights, for example ACLs (Access Control Lists). For such environments, "use
filetest" may help the permission operators to return results more consistent
with other tools.

%if %{dual_life} || %{rebuild_from_scratch}
# FIXME Filter-Simple? version?
%package Filter
Summary:        Perl source filters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          2
Version:        1.64
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Filter
%endif
%description Filter
Source filters alter the program text of a module before Perl sees it, much as
a C preprocessor alters the source text of a C program before the compiler
sees it.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Filter-Simple
Summary:        Simplified Perl source filtering
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.96
BuildArch:      noarch
Conflicts:      perl < 4:5.20.1-312
Requires:       perl(Text::Balanced) >= 1.97
Requires:       perl(warnings)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Filter_Simple
%endif
%description Filter-Simple
The Filter::Simple Perl module provides a simplified interface to
Filter::Util::Call; one that is sufficient for most common cases.
%endif

%package FindBin
Summary:        Locate a directory of an original Perl script
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.54
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_FindBin
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description FindBin
Locates the full path to the script bin directory to allow the use of paths
relative to the bin directory.

%if %{with gdbm}
%package GDBM_File
Summary:        Perl5 access to the gdbm library
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        1.24
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_GDBM_File
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description GDBM_File
GDBM_File is a module which allows Perl programs to make use of the facilities
provided by the GNU gdbm library.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Getopt-Long
Summary:        Extended processing of command line options
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        2.58
Requires:       perl(overload)
Requires:       perl(Text::ParseWords)
Requires:       perl(Pod::Usage) >= 1.14
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Getopt_Long
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.3-268
%description Getopt-Long
The Getopt::Long module implements an extended getopt function called
GetOptions(). It parses the command line from @ARGV, recognizing and removing
specified options and their possible values.  It adheres to the POSIX syntax
for command line options, with GNU extensions. In general, this means that
options have long names instead of single letters, and are introduced with
a double dash "--". Support for bundling of command line options, as was the
case with the more traditional single-letter approach, is provided but not
enabled by default.
%endif

%package Getopt-Std
Summary:        Process single-character switches with switch clustering
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.14
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Getopt_Std
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Getopt-Std
The Getopt::Std module provides functions for processing single-character
switches with switch clustering. Pass one argument which is a string
containing all switches to be recognized.

%package Hash-Util
Summary:        General-utility hash subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.32
Requires:       perl(Hash::Util::FieldHash)
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Hash_Util
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Hash-Util
Hash::Util contains special functions for manipulating hashes that don't
really warrant a keyword.

%package Hash-Util-FieldHash
Summary:        Support for inside-out classes
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.27
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Hash_Util_FieldHash
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Hash-Util-FieldHash
Hash::Util::FieldHash offers a number of functions in support of the
inside-out technique of class construction.

%package if
Summary:        Use a Perl module if a condition holds
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.61.000
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_if
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description if
The "if" module is used to conditionally load another module.

%package IO
Summary:        Perl input/output modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.55
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_IO
%endif
Conflicts:      perl < 4:5.22.0-351
%description IO
This is a collection of Perl input/output modules.

%if %{dual_life} || %{rebuild_from_scratch}
%package IO-Compress
Summary:        IO::Compress wrapper for modules
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.213
Obsoletes:      perl-Compress-Zlib <= 2.020
Provides:       perl(IO::Uncompress::Bunzip2)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_IO_Compress
%endif
BuildArch:      noarch
%description IO-Compress
This module is the base class for all IO::Compress and IO::Uncompress modules.
This module is not intended for direct use in application code. Its sole
purpose is to to be sub-classed by IO::Compress modules.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package IO-Socket-IP
Summary:        Drop-in replacement for IO::Socket::INET supporting both IPv4 and IPv6
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.43
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_IO_Socket_IP
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.20.0-303
%description IO-Socket-IP
This module provides a protocol-independent way to use IPv4 and IPv6
sockets, as a drop-in replacement for IO::Socket::INET. Most constructor
arguments and methods are provided in a backward-compatible way.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package IO-Zlib
Summary:        Perl IO:: style interface to Compress::Zlib
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        1.15
BuildRequires:  gzip
Requires:       gzip
Requires:       perl(Compress::Zlib) >= 2
Requires:       perl(IO::Handle)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_IO_Zlib
%endif
BuildArch:      noarch
%description IO-Zlib
IO::Zlib provides an IO:: style interface to Compress::Zlib and hence to
gzip/zlib-compressed files. It provides many of the same methods as the
IO::Handle interface.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package IPC-Cmd
Summary:        Finding and running system commands made easy
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          2
Version:        1.04
Requires:       perl(ExtUtils::MM::Utils)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_IPC_Cmd
%endif
BuildArch:      noarch
%description IPC-Cmd
IPC::Cmd allows you to run commands, interactively if desired, in a platform
independent way, but have them still work.
%endif

%package IPC-Open3
Summary:        Open a process for reading, writing, and error handling
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.24
Requires:       perl(Fcntl)
Requires:       perl(IO::Pipe)
Requires:       perl(POSIX)
Requires:       perl(warnings)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_IPC_Open3
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description IPC-Open3
These are functions that spawn a given command and connects the standard
output of the command for reading, standard output for writing, and standard
error output for handling the errors.

%if %{dual_life} || %{rebuild_from_scratch}
%package IPC-SysV
Summary:        Object interface to System V IPC
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.09
Requires:       perl(DynaLoader)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_IPC_SysV
%endif
Conflicts:      perl < 4:5.22.0-351
%description IPC-SysV
This is an object interface for System V messages, semaphores, and
inter-process calls.
%endif

%package I18N-Collate
Summary:        Compare 8-bit scalar data according to the current locale
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.02
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_I18N_Collate
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description I18N-Collate
This module provides you with objects that will collate according to your
national character set. This module is deprecated. See the perllocale manual
page for further information.

%package I18N-Langinfo
Summary:        Query locale information
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.24
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_I18N_Langinfo
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description I18N-Langinfo
The langinfo() function queries various locale information that can be used to
localize output and user interfaces. It uses the current underlying locale,
regardless of whether or not it was called from within the scope of "use
locale".

%package I18N-LangTags
Summary:        Functions for dealing with RFC 3066 language tags
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.45
Requires:       perl(integer)
Requires:       perl(warnings)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_I18N_LangTags
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description I18N-LangTags
Language tags are a formalism, described in RFC 3066, for declaring what
language form (language and possibly dialect) a given chunk of information is
in. This library provides functions for common tasks involving language tags
as they are needed in a variety of protocols and applications.

%if %{dual_life} || %{rebuild_from_scratch}
%package HTTP-Tiny
Summary:        A small, simple, correct HTTP/1.1 client
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.090
Requires:       perl(bytes)
Requires:       perl(Carp)
Requires:       perl(IO::Socket)
Requires:       perl(Time::Local)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_HTTP_Tiny
%endif
BuildArch:      noarch
%description HTTP-Tiny
This is a very simple HTTP/1.1 client, designed primarily for doing simple GET 
requests without the overhead of a large framework like LWP::UserAgent.
It is more correct and more complete than HTTP::Lite. It supports proxies 
(currently only non-authenticating ones) and redirection. It also correctly 
resumes after EINTR.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package JSON-PP
Summary:        JSON::XS compatible pure-Perl module
Epoch:          1
Version:        4.16
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
Requires:       perl(Data::Dumper)
Requires:       perl(Encode)
Requires:       perl(Math::BigFloat)
Requires:       perl(Math::BigInt)
Requires:       perl(Scalar::Util)
Requires:       perl(subs)
%if %{defined perl_bootstrap}
Requires:       %perl_compat 
%gendep_perl_JSON_PP
%endif
Conflicts:      perl-JSON < 2.50
%description JSON-PP
JSON::XS is the fastest and most proper JSON module on CPAN. It is written by
Marc Lehmann in C, so must be compiled and installed in the used environment.
JSON::PP is a pure-Perl module and is compatible with JSON::XS.
%endif

%package less
Summary:        Perl pragma to request less of something
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.03
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_less
%endif
Conflicts:      perl < 4:5.30.1-451
%description less
"use less ...;" is a Perl user-pragma. If you're very lucky some code you're
using will know that you asked for less CPU usage or RAM or fat or... we just
can't know.

%package lib
Summary:        Manipulate @INC at compile time
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.65
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_lib
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description lib
This module simplifies the manipulation of @INC at compile time.

%if %{dual_life} || %{rebuild_from_scratch}
%package libnet
Summary:        Perl clients for various network protocols
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        3.15
Requires:       perl(File::Basename)
Requires:       perl(IO::Socket) >= 1.05
Requires:       perl(IO::Socket::IP) >= 0.20
Requires:       perl(POSIX)
Requires:       perl(Socket) >= 2.016
Requires:       perl(utf8)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_libnet
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347
%description libnet
This is a collection of Perl modules which provides a simple and
consistent programming interface (API) to the client side of various
protocols used in the internet community.
%endif

%package libnetcfg
Summary:        Configure libnet
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          %perl_epoch
Version:        %perl_version
BuildArch:      noarch
%if %{defined perl_bootstrap}
%gendep_perl_libnetcfg
%endif
Conflicts:      perl-devel < 4:5.22.0-347
%description libnetcfg
The libnetcfg utility can be used to configure the libnet.

%package locale
Summary:        Pragma to use or avoid POSIX locales for built-in operations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.13
Requires:       perl(Carp)
Requires:       perl(POSIX)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_locale
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description locale
This pragma tells the compiler to enable (or disable) the use of POSIX locales
for built-in operations (for example, LC_CTYPE for regular expressions,
LC_COLLATE for string comparison, and LC_NUMERIC for number formatting). Each
"use locale" or "no locale" affects statements to the end of the enclosing
block.

%if %{dual_life} || %{rebuild_from_scratch}
%package Locale-Maketext
Summary:        Framework for localization
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.33
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Locale_Maketext
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.3-268
%description Locale-Maketext
It is a common feature of applications (whether run directly, or via the Web)
for them to be "localized" -- i.e., for them to present an English interface
to an English-speaker, a German interface to a German-speaker, and so on for
all languages it's programmed with. Locale::Maketext is a framework for
software localization; it provides you with the tools for organizing and
accessing the bits of text and text-processing code that you need for
producing localized applications.
%endif

%package Locale-Maketext-Simple
Summary:        Simple interface to Locale::Maketext::Lexicon
License:        MIT
Epoch:          1
Version:        0.21
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Locale_Maketext_Simple
%endif
BuildArch:      noarch
%description Locale-Maketext-Simple
This module is a simple wrapper around Locale::Maketext::Lexicon, designed
to alleviate the need of creating Language Classes for module authors.

%if %{dual_life} || %{rebuild_from_scratch}
%package Math-BigInt
Summary:        Arbitrary-size integer and float mathematics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        2.0050.02
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Math_BigInt
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(Math::BigInt\\)\\s*$
%description Math-BigInt
This provides Perl modules for arbitrary-size integer and float mathematics.

%package Math-BigInt-FastCalc
Summary:        Math::BigInt::Calc XS implementation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.502.000
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Math_BigInt_FastCalc
%endif
Conflicts:      perl < 4:5.22.0-348
%description Math-BigInt-FastCalc
This package provides support for faster big integer calculations.
%endif

%package Math-Complex
Summary:        Complex numbers and trigonometric functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.63
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Math_Complex
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-348
%description Math-Complex
This package lets you create and manipulate complex numbers. By default, Perl
limits itself to real numbers, but an extra "use" statement brings full
complex support, along with a full set of mathematical functions typically
associated with and/or extended to complex numbers.

%package Memoize
Summary:        Transparently speed up functions by caching return values
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.17
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Memoize
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-350
%description Memoize
Memoizing a function makes it faster by trading space for time. It does
this by caching the return values of the function in a table. If you call
the function again with the same arguments, memoize jumps in and gives
you the value out of the table, instead of letting the function compute
the value all over again.

%package meta-notation
Summary:        Change nonprintable characters below 0x100 into printables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        %{perl_version}
BuildArch:      noarch
Provides:       perl(meta_notation) = %{perl_version}
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_meta_notation
%endif
Conflicts:      perl < 4:5.30.1-451
%description meta-notation
Returns a copy of the input string with the nonprintable characters below
0x100 changed into printables. Any ASCII printables or above 0xFF are
unchanged.

%if %{dual_life} || %{rebuild_from_scratch}
%package MIME-Base64
Summary:        Encoding and decoding of Base64 and quoted-printable strings
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND MIT
Epoch:          0
Version:        3.16
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_MIME_Base64
%endif
Conflicts:      perl < 4:5.22.0-347
%description MIME-Base64
This package contains a Base64 encoder/decoder and a quoted-printable
encoder/decoder. These encoding methods are specified in RFC 2045 - MIME
(Multipurpose Internet Mail Extensions).
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Module-CoreList
Summary:        What modules are shipped with versions of perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        5.20260308
Requires:       perl(List::Util)
Requires:       perl(version) >= 0.88
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Module_CoreList
%endif
BuildArch:      noarch
%description Module-CoreList
Module::CoreList provides information on which core and dual-life modules
are shipped with each version of perl.

%package Module-CoreList-tools
Summary:        Tool for listing modules shipped with perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        5.20260308
Requires:       perl(feature)
Requires:       perl(version) >= 0.88
Requires:       perl-Module-CoreList = %{epoch}:%{version}-%{release}
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Module_CoreList_tools
%endif
Conflicts:      perl-Module-CoreList < 1:5.020001-310
BuildArch:      noarch
%description Module-CoreList-tools
This package provides a corelist(1) tool which can be used to query what
modules were shipped with given perl version.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Module-Load
Summary:        Runtime require of both modules and files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        0.36
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Module_Load
%endif
BuildArch:      noarch
%description Module-Load
Module::Load eliminates the need to know whether you are trying to require
either a file or a module.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Module-Load-Conditional
Summary:        Looking up module information / loading at runtime
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.74
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Module_Load_Conditional
%endif
BuildArch:      noarch
%description Module-Load-Conditional
Module::Load::Conditional provides simple ways to query and possibly load any
of the modules you have installed on your system during runtime.
%endif

%package Module-Loaded
Summary:        Mark modules as loaded or unloaded
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        0.08
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Module_Loaded
%endif
BuildArch:      noarch
%description Module-Loaded
When testing applications, often you find yourself needing to provide
functionality in your test environment that would usually be provided by
external modules. Rather than munging the %%INC by hand to mark these external
modules as loaded, so they are not attempted to be loaded by perl, this module
offers you a very simple way to mark modules as loaded and/or unloaded.

%if %{dual_life} || %{rebuild_from_scratch}
%package Module-Metadata
Summary:        Gather package and POD information from perl module files
Epoch:          0
Version:        1.000038
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Module_Metadata
%endif
%description Module-Metadata
Gather package and POD information from perl module files
%endif

%package mro
Summary:        Method resolution order
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.29
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_mro
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description mro
The "mro" name space provides several utilities for dealing with method
resolution order and method caching in general.

%if %{with gdbm}
%package NDBM_File
Summary:        Tied access to ndbm files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.18
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_NDBM_File
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description NDBM_File
NDBM_File establishes a connection between a Perl hash variable and a file in
ndbm format. You can manipulate the data in the file just as if it were in
a Perl hash, but when your program exits, the data will remain in the file, to
be used the next time your program runs.
%endif

%package Net
Summary:        By-name interface to Perl built-in network resolver
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.04
BuildArch:      noarch
Requires:       perl(Socket)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Net
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Net
This package provide object-oriented interface to Perl built-in gethost*(),
getnet*(), getproto*(), and getserv*() functions.

%if %{dual_life} || %{rebuild_from_scratch}
%package Net-Ping
Summary:        Check a remote host for reachability
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.76
Requires:       perl(IO::Socket::INET)
Suggests:       perl(Net::Ping::External)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Net_Ping
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-350
%description Net-Ping
Net::Ping module contains methods to test the reachability of remote hosts on
a network.
%endif

%package NEXT
Summary:        Pseudo-class that allows method redispatch
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.69
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_NEXT
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description NEXT
The NEXT module adds a pseudo-class named "NEXT" to any program that uses it.
If a method "m" calls "$self->NEXT::m()", the call to "m" is redispatched as
if the calling method had not originally been found.

%if %{with gdbm}
%package ODBM_File
Summary:        Tied access to odbm files
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.20
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ODBM_File
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description ODBM_File
ODBM_File establishes a connection between a Perl hash variable and a file in
odbm format. You can manipulate the data in the file just as if it were in
a Perl hash, but when your program exits, the data will remain in the file, to
be used the next time your program runs.
%endif

%package Opcode
Summary:        Disable named opcodes when compiling a perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.69
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Opcode
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Opcode
The Opcode module allows you to define an operator mask to be in effect when
perl next compiles any code. Attempting to compile code which contains
a masked opcode will cause the compilation to fail with an error. The code
will not be executed.

%package open
Summary:        Perl pragma to set default PerlIO layers for input and output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.13
Requires:       perl(Carp)
Requires:       perl(Encode)
Requires:       perl(encoding)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_open
%endif
Conflicts:      perl < 4:5.20.2-326
BuildArch:      noarch
%description open
The "open" pragma serves as one of the interfaces to declare default "layers"
(also known as "disciplines") for all I/O.

%package overload
Summary:        Overloading Perl operations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.40
BuildArch:      noarch
Requires:       perl(mro)
Requires:       perl(Scalar::Util)
Requires:       perl(overloading)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_overload
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description overload
The "overload" pragma allows overloading of Perl operators for a class. To
overload built-in functions, see "Overriding Built-in Functions" in perlsub
POD instead.

%package overloading
Summary:        Perl pragma to lexically control overloading
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.02
BuildArch:      noarch
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_overloading
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description overloading
Overloading pragma allows you to lexically disable or enable overloading.

%if %{dual_life} || %{rebuild_from_scratch}
%package parent
Summary:        Establish an ISA relationship with base classes at compile time
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        0.244
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_parent
%endif
BuildArch:      noarch
%description parent
parent allows you to both load one or more modules, while setting up
inheritance from those modules at the same time. Mostly similar in effect to:

    package Baz;

    BEGIN {
        require Foo;
        require Bar;

        push @ISA, qw(Foo Bar);
    }
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Params-Check
Summary:        Generic input parsing/checking mechanism
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        0.38
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Params_Check
%endif
BuildArch:      noarch
%description Params-Check
Params::Check is a generic input parsing/checking mechanism.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package PathTools
Summary:        PathTools Perl module (Cwd, File::Spec)
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-3-Clause
Epoch:          0
Version:        3.94
Requires:       perl(Carp)
Requires:       perl(Errno)
Requires:       perl(Scalar::Util)
Recommends:     perl(XSLoader)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_PathTools
%endif
%description PathTools
PathTools Perl module (Cwd, File::Spec).
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package perlfaq
Summary:        Frequently asked questions about Perl
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND LicenseRef-Fedora-Public-Domain
Epoch:          0
Version:        5.20250619
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_perlfaq
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347
%description perlfaq
The perlfaq comprises several documents that answer the most commonly asked
questions about Perl and Perl programming.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package PerlIO-via-QuotedPrint
Summary:        PerlIO layer for quoted-printable strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.10
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_PerlIO_via_QuotedPrint
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347
%description PerlIO-via-QuotedPrint
This module implements a PerlIO layer that works on files encoded in the
quoted-printable format. It will decode from quoted-printable while
reading from a handle, and it will encode as quoted-printable while
writing to a handle.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Perl-OSType
Summary:        Map Perl operating system names to generic types
Version:        1.010
Epoch:          0
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Perl_OSType
%endif
BuildArch:      noarch
%description Perl-OSType
Modules that provide OS-specific behaviors often need to know if the current
operating system matches a more generic type of operating systems. For example,
'linux' is a type of 'Unix' operating system and so is 'freebsd'.
This module provides a mapping between an operating system name as given by $^O
and a more generic type. The initial version is based on the OS type mappings
provided in Module::Build and ExtUtils::CBuilder (thus, Microsoft operating
systems are given the type 'Windows' rather than 'Win32').
%endif

%package ph
Summary:        Selected system header files converted to Perl headers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        %{perl_version}
Requires:       perl-libs%{?_isa} = %{perl_epoch}:%{perl_version}-%{release}
Requires:       perl(warnings)
Provides:       perl(sys/ioctl.ph) = %{perl_version}
Provides:       perl(sys/syscall.ph) = %{perl_version}
Provides:       perl(syscall.ph) = %{perl_version}
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_ph
%endif
Conflicts:      perl < 4:5.30.1-451
%description ph
Contemporary Perl still refers to some Perl header (ph) files although it does
not build them anymore. This is a prebuilt collection of the referred files.
If you miss other ones, you can generate them with h2ph tool from perl-utils
package.

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Checker
Summary:        Check POD documents for syntax errors
Epoch:          4
Version:        1.77
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Pod_Checker
%endif
BuildArch:      noarch
%description Pod-Checker
Module and tools to verify POD documentation contents for compliance with the
Plain Old Documentation format specifications.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Escapes
Summary:        Resolve POD escape sequences
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        1.07
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Pod_Escapes
%endif
BuildArch:      noarch
%description Pod-Escapes
This module provides things that are useful in decoding Pod E<...> sequences.
%endif

%package Pod-Functions
Summary:        Group Perl functions as in perlfunc POD
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.14
BuildArch:      noarch
Requires:       perl-libs = %{perl_epoch}:%{perl_version}-%{release}
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Pod_Functions
%endif
Conflicts:      perl < 4:5.30.1-451
%description Pod-Functions
This module enumerates the Perl functions that are documented in perlfunc POD.

%package Pod-Html
Summary:        Convert POD files to HTML
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.35
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Pod_Html
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-350
%description Pod-Html
This package converts files from POD format (see perlpod) to HTML format. It
can automatically generate indexes and cross-references, and it keeps a cache
of things it knows how to cross-reference.

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Perldoc
Summary:        Look up Perl documentation in Pod format
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        3.28.01
%if %{with perl_enables_groff}
Requires:       groff-base
%endif
Requires:       perl(File::Temp) >= 0.22
Requires:       perl(HTTP::Tiny)
Requires:       perl(IO::Handle)
Requires:       perl(IPC::Open3)
Requires:       perl(Pod::Simple::Checker)
Requires:       perl(Pod::Simple::RTF) >= 3.16
Requires:       perl(Pod::Simple::XMLOutStream) >= 3.16
Requires:       perl(Text::ParseWords)
Requires:       perl(Symbol)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Pod_Perldoc
%endif
BuildArch:      noarch
%description Pod-Perldoc
perldoc looks up a piece of documentation in .pod format that is embedded
in the perl installation tree or in a perl script, and displays it via
"groff -man | $PAGER". This is primarily used for the documentation for
the perl library modules.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Simple
Summary:        Framework for parsing POD documentation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        3.45
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Pod_Simple
%endif
BuildArch:      noarch
%description Pod-Simple
Pod::Simple is a Perl library for parsing text in the Pod ("plain old
documentation") markup language that is typically used for writing
documentation for Perl and for Perl modules.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Pod-Usage
Summary:        Print a usage message from embedded pod documentation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          4
Version:        2.05
Requires:       perl-Pod-Perldoc
Requires:       perl(Pod::Text)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Pod_Usage
%endif
BuildArch:      noarch
%description Pod-Usage
pod2usage will print a usage message for the invoking script (using its
embedded POD documentation) and then exit the script with the desired exit
status. The usage message printed may have any one of three levels of
"verboseness": If the verbose level is 0, then only a synopsis is printed.
If the verbose level is 1, then the synopsis is printed along with a
description (if present) of the command line options and arguments. If the
verbose level is 2, then the entire manual page is printed.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package podlators
Summary:        Format POD source into various output formats
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND FSFAP
Epoch:          1
Version:        6.0.2
BuildArch:      noarch
Requires:       perl(File::Spec) >= 0.8
Requires:       perl(Pod::Simple) >= 3.06
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_podlators
%endif
Conflicts:      perl < 4:5.16.1-234
%description podlators
This package contains Pod::Man and Pod::Text modules which convert POD input
to *roff source output, suitable for man pages, or plain text.  It also
includes several sub-classes of Pod::Text for formatted output to terminals
with various capabilities.
%endif

%package POSIX
Summary:        Perl interface to IEEE Std 1003.1
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.23
Requires:       perl(Carp)
Requires:       perl(locale)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_POSIX
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description POSIX
The POSIX module permits you to access all (or nearly all) the standard POSIX
1003.1 identifiers. Many of these identifiers have been given Perl interfaces.

%package Safe
Summary:        Compile and execute code in restricted compartments
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.47
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Safe
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Safe
The Safe extension module allows the creation of compartments in which Perl
code can be evaluated. Please note that the restriction is not suitable for
security purposes.

%if %{dual_life} || %{rebuild_from_scratch}
%package Scalar-List-Utils
Summary:        A selection of general-utility scalar and list subroutines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          5
Version:        1.69
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Scalar_List_Utils
%endif
%description Scalar-List-Utils
Scalar::Util and List::Util contain a selection of subroutines that people have
expressed would be nice to have in the perl core, but the usage would not
really be high enough to warrant the use of a keyword, and the size so small
such that being individual extensions would be wasteful.
%endif

%package Search-Dict
Summary:        Search for a key in a dictionary file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.08
Requires:       perl(feature)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Search_Dict
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Search-Dict
This module sets file position in a file handle to be first line greater than
or equal (string-wise) to a key.

%package SelectSaver
Summary:        Save and restore selected file handle
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.02
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_SelectSaver
%endif
Conflicts:      perl < 4:5.30.1-451
%description SelectSaver
A "SelectSaver" object contains a reference to the file handle that was
selected when it was created. When the object is destroyed, it re-selects the
file handle that was selected when it was created.

%package SelfLoader
Summary:        Load functions only on demand
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.28
BuildArch:      noarch
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_SelfLoader
%endif
Conflicts:      perl < 4:5.22.0-351
%description SelfLoader
This Perl module tells its users that functions in a package are to be
autoloaded from after the "__DATA__" token. See also "Autoloading" in
perlsub.

%package sigtrap
Summary:        Perl pragma to enable simple signal handling
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.10
BuildArch:      noarch
Requires:       perl(meta_notation) = %{perl_version}
Requires:       perl(Symbol)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_sigtrap
%endif
Conflicts:      perl < 4:5.30.1-451
%description sigtrap
The sigtrap pragma is a simple interface for installing signal handlers.

%if %{dual_life} || %{rebuild_from_scratch}
%package Socket
Summary:        C socket.h defines and structure manipulators
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          4
Version:        2.038
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Socket
%endif
%description Socket
This module is just a translation of the C socket.h file.  Unlike the old
mechanism of requiring a translated socket.ph file, this uses the h2xs program
(see the Perl source distribution) and your native C compiler.  This means
that it has a far more likely chance of getting the numbers right.  This
includes all of the commonly used pound-defines like AF_INET, SOCK_STREAM, etc.
%endif

%package sort
Summary:        Perl pragma to control sort() behavior
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.06
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(warnings)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_sort
%endif
Conflicts:      perl < 4:5.30.1-451
%description sort
With the "sort" pragma you can control the behavior of the builtin "sort()"
function.

%if %{dual_life} || %{rebuild_from_scratch}
%package Storable
Summary:        Persistence for Perl data structures
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        3.37
Requires:       perl(Carp)
Requires:       perl(Config)
Requires:       perl(Fcntl)
Requires:       perl(IO::File)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Storable
%endif
Conflicts:      perl < 4:5.16.3-274
%description Storable
The Storable package brings persistence to your Perl data structures
containing scalar, array, hash or reference objects, i.e. anything that
can be conveniently stored to disk and retrieved at a later time.
%endif

%package subs
Summary:        Perl pragma to predeclare subroutine names
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.04
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_subs
%endif
Conflicts:      perl < 4:5.30.1-451
%description subs
This will predeclare all the subroutines whose names are in the list,
allowing you to use them without parentheses (as list operators) even
before they're declared.

%package Symbol
Summary:        Manipulate Perl symbols and their names
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.09
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Symbol
%endif
Conflicts:      perl < 4:5.30.1-451
%description Symbol
The Symbol module provides functions for manipulating Perl symbols.

%package Sys-Hostname
Summary:        Try every conceivable way to get a hostname
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.25
Suggests:       perl(POSIX)
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Sys_Hostname
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Sys-Hostname
It attempts several methods of getting the system hostname and then caches the
result.

%if %{dual_life} || %{rebuild_from_scratch}
%package Sys-Syslog
Summary:        Perl interface to the UNIX syslog(3) calls
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.36
Requires:       perl(XSLoader)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Sys_Syslog
%endif
Conflicts:      perl < 4:5.16.3-269
%description Sys-Syslog
Sys::Syslog is an interface to the UNIX syslog(3) function. Call syslog() with
a string priority and a list of printf() arguments just like at syslog(3).
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Term-ANSIColor
Summary:        Color screen output using ANSI escape sequences
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        5.01
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Term_ANSIColor
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.18.2-302
%description Term-ANSIColor
This module has two interfaces, one through color() and colored() and the
other through constants. It also offers the utility functions uncolor(),
colorstrip(), colorvalid(), and coloralias(), which have to be explicitly
imported to be used.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Term-Cap
Summary:        Perl termcap interface
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.18
Requires:       ncurses
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Term_Cap
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347
%description Term-Cap
These are low-level functions to extract and use capabilities from a terminal
capability (termcap) database.
%endif

%package Term-Complete
Summary:        Perl word completion
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.403
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Term_Complete
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Term-Complete
"Complete" routine provides word completion on a list of words in the array.

%package Term-ReadLine
Summary:        Perl interface to various read-line packages
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.17
Requires:       perl(Term::Cap)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Term_ReadLine
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Term-ReadLine
This package is just a front end to some other packages. It's a stub to
set up a common interface to the various read-line implementations found
on CPAN (under the "Term::ReadLine::*" name space).

%if %{dual_life} || %{rebuild_from_scratch}
%package Term-Table
Summary:        Format a header and rows into a table
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.024
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Term_Table
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.39.10-507
%description Term-Table
This Perl module is able to format rows of data into tables.
%endif

%package Test
Summary:        Simple framework for writing test scripts
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.31
Requires:       perl(File::Temp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Test
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-351
%description Test
The Test Perl module simplifies the task of writing test files for Perl modules,
such that their output is in the format that Test::Harness expects to see.

%if %{dual_life} || %{rebuild_from_scratch}
%package Test-Harness
Summary:        Run Perl standard test scripts with statistics
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        3.50
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Test_Harness
%endif
BuildArch:      noarch
%description Test-Harness
Run Perl standard test scripts with statistics.
Use TAP::Parser, Test::Harness package was whole rewritten.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Test-Simple
Summary:        Basic utilities for writing tests
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND CC0-1.0 AND LicenseRef-Fedora-Public-Domain
Epoch:          3
Version:        1.302210
Requires:       perl(Data::Dumper)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Test_Simple
%endif
BuildArch:      noarch
%description Test-Simple
Basic utilities for writing tests.
%endif

%package Text-Abbrev
Summary:        Create an abbreviation table from a list
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.02
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Text_Abbrev
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Text-Abbrev
It stores all unambiguous truncations of each element of a list as keys in
an associative array. The values are the original list elements.

%if %{dual_life} || %{rebuild_from_scratch}
%package Text-Balanced
Summary:        Extract delimited text sequences from strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.06
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Text_Balanced
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.22.0-347
%description Text-Balanced
These Perl subroutines may be used to extract a delimited substring, possibly
after skipping a specified prefix string.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Text-ParseWords
Summary:        Parse text into an array of tokens or array of arrays
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        3.31
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Text_ParseWords
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-256
%description Text-ParseWords
Parse text into an array of tokens or array of arrays.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Text-Tabs+Wrap
Summary:        Expand tabs and do simple line wrapping
License:        TTWL
Epoch:          0
Version:        2024.001
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Text_Tabs_Wrap
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.20.2-325
%description Text-Tabs+Wrap
Text::Tabs performs the same job that the UNIX expand(1) and unexpand(1)
commands do: adding or removing tabs from a document.

Text::Wrap::wrap() will reformat lines into paragraphs. All it does is break
up long lines, it will not join short lines together.
%endif

%package Thread
Summary:        Manipulate threads in Perl (for old code only)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        3.06
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Thread
%endif
Conflicts:      perl < 4:5.30.1-451
%description Thread
This Thread module served as the front end to the old-style thread model,
called 5005threads, that has been removed in version 5.10.

For old code and interim backwards compatibility, the Thread module has been
reworked to function as a front end for the new interpreter threads (ithreads)
model. However, some previous functionality is not available. Further, the
data sharing models between the two thread models are completely different,
and anything to do with data sharing has to be thought differently.

You are strongly encouraged to migrate any existing threaded code to the new
model (i.e., use the threads and threads::shared modules) as soon as possible.

%if %{dual_life} || %{rebuild_from_scratch}
%package Thread-Queue
Summary:        Thread-safe queues
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        3.14
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Thread_Queue
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.2-257
%description Thread-Queue
This module provides thread-safe FIFO queues that can be accessed safely by
any number of threads.
%endif

%package Tie
Summary:        Base classes for tying variables
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        4.6
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Tie
%endif
Conflicts:      perl < 4:5.30.1-451
%description Tie
These are Perl modules that helps connecting classes with arrays, hashes,
handles, and scalars.

%package Tie-File
Summary:        Access the lines of a disk file via a Perl array
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.10
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Tie_File
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Tie-File
Tie::File represents a regular text file as a Perl array. Each element in the
array corresponds to a record in the file. The first line of the file is
element 0 of the array; the second line is element 1, and so on.  The file is
not loaded into memory, so this will work even for gigantic files.  Changes to
the array are reflected in the file immediately.

%package Tie-Memoize
Summary:        Add data to a hash when needed
License:        GPL-2.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.1
Requires:       perl(Carp)
Requires:       perl(Tie::ExtraHash)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Tie_Memoize
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Tie-Memoize
This package allows a tied hash to load its values automatically on the first
access, and to use the cached value on the following accesses.

%if %{dual_life} || %{rebuild_from_scratch}
%package Tie-RefHash
Summary:        Use references as hash keys
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.41
Requires:       perl(overload)
Suggests:       perl(Scalar::Util)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Tie_RefHash
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Tie-RefHash
This module provides the ability to use references as hash keys if you first
"tie" the hash variable to this module. Normally, only the keys of the tied
hash itself are preserved as references; to use references as keys in
hashes-of-hashes, use Tie::RefHash::Nestable, included as part of
Tie::RefHash.
%endif

%package Time
Summary:        By-name interface to Perl built-in time functions
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.04
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Time
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Time
This package provides an object-oriented interface to Perl built-in gmtime()
and localtime () functions.

%if %{dual_life} || %{rebuild_from_scratch}
%package Time-HiRes
Summary:        High resolution alarm, sleep, gettimeofday, interval timers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          4
Version:        1.9778
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Time_HiRes
%endif
Conflicts:      perl < 4:5.16.3-271
%description Time-HiRes
The Time::HiRes module implements a Perl interface to the usleep, nanosleep,
ualarm, gettimeofday, and setitimer/getitimer system calls, in other words,
high resolution time and timers.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Time-Local
Summary:        Efficiently compute time from local and GMT time
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          2
Version:        1.350
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Time_Local
%endif
BuildArch:      noarch
Conflicts:      perl < 4:5.16.3-262
%description Time-Local
This module provides functions that are the inverse of built-in perl functions
localtime() and gmtime(). They accept a date as a six-element array, and
return the corresponding time(2) value in seconds since the system epoch
(Midnight, January 1, 1970 GMT on Unix, for example). This value can be
positive or negative, though POSIX only requires support for positive values,
so dates before the system's epoch may not work on all operating systems.
%endif

%package Time-Piece
Summary:        Time objects from localtime and gmtime
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND BSD-2-Clause-Views
Epoch:          0
Version:        1.3600
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Time_Piece
%endif
%description Time-Piece
The Time::Piece module replaces the standard localtime and gmtime functions
with implementations that return objects.  It does so in a backwards compatible
manner, so that using localtime or gmtime as documented in perlfunc still
behave as expected.

%package Thread-Semaphore
Summary:        Thread-safe semaphores
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        2.13
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Thread_Semaphore
%endif
BuildArch:      noarch
Conflicts:      perl-interpreter < 4:5.30.1-451
%description Thread-Semaphore
Semaphores provide a mechanism to regulate access to resources. Unlike locks,
semaphores aren't tied to particular scalars, and so may be used to control
access to anything you care to use them for. Semaphores don't limit their
values to zero and one, so they can be used to control access to some resource
that there may be more than one of (e.g., file handles). Increment and
decrement amounts aren't fixed at one either, so threads can reserve or return
multiple resources at once.

%if %{dual_life} || %{rebuild_from_scratch}
%package threads
Summary:        Perl interpreter-based threads
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          1
Version:        2.43
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_threads
%endif
%description threads
Since Perl 5.8, thread programming has been available using a model called
interpreter threads  which provides a new Perl interpreter for each thread,
and, by default, results in no data or state information being shared between
threads.

(Prior to Perl 5.8, 5005threads was available through the Thread.pm API. This
threading model has been deprecated, and was removed as of Perl 5.10.0.)

As just mentioned, all variables are, by default, thread local. To use shared
variables, you need to also load threads::shared.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package threads-shared
Summary:        Perl extension for sharing data structures between threads
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.70
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_threads_shared
%endif
%description threads-shared
By default, variables are private to each thread, and each newly created thread
gets a private copy of each existing variable. This module allows you to share
variables across different threads (and pseudo-forks on Win32). It is used
together with the threads module.  This module supports the sharing of the
following data types only: scalars and scalar refs, arrays and array refs, and
hashes and hash refs.
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Unicode-Collate
Summary:        Unicode Collation Algorithm
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND Unicode-DFS-2015
Epoch:          0
Version:        1.31
Requires:       perl(Unicode::Normalize)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Unicode_Collate
%endif
Conflicts:      perl < 4:5.22.0-347
%description Unicode-Collate
This package is Perl implementation of Unicode Technical Standard #10 (Unicode
Collation Algorithm).
%endif

%if %{dual_life} || %{rebuild_from_scratch}
%package Unicode-Normalize
Summary:        Unicode Normalization Forms
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.32
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Unicode_Normalize
%endif
Conflicts:      perl < 4:5.22.0-347
%description Unicode-Normalize
This package provides Perl functions that can convert strings into various
Unicode normalization forms as defined in Unicode Standard Annex #15.
%endif

%package Unicode-UCD
Summary:        Unicode character database
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        0.81
BuildArch:      noarch
Requires:       perl(Storable)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_Unicode_UCD
%endif
Conflicts:      perl < 4:5.30.1-451
%description Unicode-UCD
The Unicode::UCD module offers a series of functions that provide a simple
interface to the Unicode Character Database.

%package User-pwent
Summary:        By-name interface to Perl built-in user name resolver
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.05
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_User_pwent
%endif
Conflicts:      perl-interpreter < 4:5.30.1-451
%description User-pwent
This package provides an object-oriented interface to Perl build-in getgr*()
and getpw*() functions.

%package vars
Summary:        Perl pragma to predeclare global variable names
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.05
BuildArch:      noarch
Requires:       perl(Carp)
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_vars
%endif
Conflicts:      perl < 4:5.30.1-451
%description vars
This pragma will predeclare all the variables whose names are in the
list, allowing you to use them under "use strict", and disabling any
typo warnings for them.

For use with variables in the current package for a single scope, the
functionality provided by this pragma has been superseded by "our"
declarations, available in Perl v5.6.0 or later, and use of this pragma is
discouraged.

%if %{dual_life} || %{rebuild_from_scratch}
%package version
Summary:        Perl extension for Version Objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          9
Version:        0.99.33
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_version
%endif
BuildArch:      noarch
%description version
Perl extension for Version Objects
%endif

%package vmsish
Summary:        Perl pragma to control VMS-specific language features
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Epoch:          0
Version:        1.04
BuildArch:      noarch
%if %{defined perl_bootstrap}
Requires:       %perl_compat
%gendep_perl_vmsish
%endif
Conflicts:      perl < 4:5.30.1-451
%description vmsish
The "vmsish" pragma control VMS-specific features of the Perl language. If
you're not running VMS, this module does nothing.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n perl-%{perl_version}
%patch -P1 -p1
%ifarch %{multilib_64_archs}
%patch -P2 -p1
%endif
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P200 -p1
%patch -P201 -p1
%patch -P202 -p1

%if !%{defined perl_bootstrap}
# Local patch tracking
perl -x patchlevel.h \
    'Fedora Patch1: Removes date check, Fedora/RHEL specific' \
%ifarch %{multilib_64_archs}
    'Fedora Patch2: support for libdir64' \
%endif
    'Fedora Patch3: use libresolv instead of libbind' \
    'Fedora Patch4: USE_MM_LD_RUN_PATH' \
    'Fedora Patch5: Provide MM::maybe_command independently (bug #1129443)' \
    'Fedora Patch6: Dont run one io test due to random builder failures' \
    'Fedora Patch8: Define SONAME for libperl.so' \
    'Fedora Patch9: Install libperl.so to -Dshrpdir value' \
    'Fedora Patch10: Make *DBM_File desctructors thread-safe (RT#61912)' \
    'Fedora Patch11: Replace EU::MakeMaker dependency with EU::MM::Utils in IPC::Cmd (bug #1129443)' \
    'Fedora Patch12: Link XS modules to pthread library to fix linking with -z defs' \
    'Fedora Patch13: Pass the correct CFLAGS to dtrace' \
    'Fedora Patch200: Link XS modules to libperl.so with EU::CBuilder on Linux' \
    'Fedora Patch201: Link XS modules to libperl.so with EU::MM on Linux' \
    'Fedora Patch202: Add definition of OPTIMIZE to .ph files' \
    %{nil}
%endif

#copy the example script
install -m 0644 %{SOURCE5} .

#copy Pod-Html license clarification
cp %{SOURCE6} .

# Copy config.over to override Configure's guesses.
cp %{SOURCE8} .

#
# Candidates for doc recoding (need case by case review):
# find . -name "*.pod" -o -name "README*" -o -name "*.pm" | xargs file -i | grep charset= | grep -v '\(us-ascii\|utf-8\)'
recode()
{
        iconv -f "${2:-iso-8859-1}" -t utf-8 < "$1" > "${1}_"
        touch -r "$1" "${1}_"
        mv -f "${1}_" "$1"
}
# TODO iconv fail on this one
##recode README.tw big5
#recode pod/perlebcdic.pod
#recode pod/perlhack.pod
#recode pod/perlhist.pod
#recode pod/perlthrtut.pod
#recode AUTHORS

find . -name \*.orig -exec rm -fv {} \;

# Configure Compress::Zlib to use system zlib
sed -i 's|BUILD_ZLIB      = True|BUILD_ZLIB      = False|
    s|INCLUDE         = ./zlib-src|INCLUDE         = %{_includedir}|
    s|LIB             = ./zlib-src|LIB             = %{_libdir}|' \
    cpan/Compress-Raw-Zlib/config.in

# Ensure that we never accidentally bundle zlib or bzip2
rm -rf cpan/Compress-Raw-Zlib/zlib-src
rm -rf cpan/Compress-Raw-Bzip2/bzip2-src
sed -i '/\(bzip2\|zlib\)-src/d' MANIFEST

%if !%{with gdbm}
# Do not install anything requiring NDBM_File if NDBM is not available.
rm -rf 'cpan/Memoize/Memoize/NDBM_File.pm'
sed -i '\|cpan/Memoize/Memoize/NDBM_File.pm|d' MANIFEST
%endif

%build

echo "RPM Build arch: %{_arch}"
%global privlib     %{_prefix}/share/perl5
%global archlib     %{_libdir}/perl5
%if 0%{?flatpak_runtime}
%global perl_vendorlib  /app/%{_lib}/perl5/vendor_perl
%global perl_vendorarch /app/share/perl5/vendor_perl
%else
%global perl_vendorlib  %{privlib}/vendor_perl
%global perl_vendorarch %{archlib}/vendor_perl
%endif
%global perl_abi    %(echo '%{perl_version}' | sed 's/^\\([^.]*\\.[^.]*\\).*/\\1/')
/bin/sh Configure -des \
        -Doptimize="none" \
        -Dccflags="$RPM_OPT_FLAGS" \
        -Dldflags="$RPM_LD_FLAGS" \
        -Dccdlflags="-Wl,--enable-new-dtags $RPM_LD_FLAGS" \
        -Dlddlflags="-shared $RPM_LD_FLAGS" \
        -Dshrpdir="%{_libdir}" \
        -DDEBUGGING=-g \
        -Dversion=%{perl_version} \
        -Dmyhostname=localhost \
        -Dperladmin=root@localhost \
        -Dcc='%{__cc}' \
        -Dcf_by='Red Hat, Inc.' \
        -Dprefix=%{_prefix} \
        -Dman1dir="%{_mandir}/man1" \
        -Dman3dir="%{_mandir}/man3" \
        -Dvendorprefix=%{_prefix} \
        -Dsiteprefix=%{_prefix}/local \
        -Dsitelib="%{_prefix}/local/share/perl5/%{perl_abi}" \
        -Dsitearch="%{_prefix}/local/%{_lib}/perl5/%{perl_abi}" \
        -Dprivlib="%{privlib}" \
        -Dvendorlib="%{perl_vendorlib}" \
        -Darchlib="%{archlib}" \
        -Dvendorarch="%{perl_vendorarch}" \
        -Darchname=%{perl_archname} \
%if 0%{?flatpak}
        -Dotherlibdirs="/usr/share/perl5/vendor_perl:/usr/%{_lib}/perl5/vendor_perl:/usr/share/perl5:/usr/%{_lib}/perl5" \
%endif
%if 0%{?flatpak_runtime}
        -Dotherlibdirs=%{archlib}/vendor_perl:%{privlib}/vendor_perl \
        -Dvendorprefix=/app \
%endif
%ifarch %{multilib_64_archs}
        -Dlibpth="/usr/local/lib64 /lib64 %{_prefix}/lib64" \
%endif
%ifarch sparc sparcv9
        -Ud_longdbl \
%endif
        -Duseshrplib \
        -Dusethreads \
        -Duseithreads \
%if %{with perl_enables_systemtap}
        -Dusedtrace='/usr/bin/dtrace' \
%else
        -Uusedtrace \
%endif
        -Duselargefiles \
        -Dd_semctl_semun \
%if %{with bdb}
        -Di_db \
%endif
%if %{with gdbm}
        -Ui_ndbm \
        -Di_gdbm \
%endif
        -Di_shadow \
        -Di_syslog \
        -Dman3ext=3pm \
        -Duseperlio \
        -Dinstallusrbinperl=n \
        -Ubincompat5005 \
        -Uversiononly \
        -Dpager='/usr/bin/less -isr' \
        -Dd_gethostent_r_proto -Ud_endhostent_r_proto -Ud_sethostent_r_proto \
        -Ud_endprotoent_r_proto -Ud_setprotoent_r_proto \
        -Ud_endservent_r_proto -Ud_setservent_r_proto \
        -Dscriptdir='%{_bindir}' \
        -Dusesitecustomize \
%ifarch %{multilib_64_archs}
        -Duse64bitall \
%endif
        -Duse64bitint
BUILD_BZIP2=0
BZIP2_LIB=%{_libdir}
export BUILD_BZIP2 BZIP2_LIB
%global soname libperl.so.%{perl_abi}
test -L %soname || ln -s libperl.so %soname
%ifarch sparc64 %{arm}
make
%else
make %{?_smp_mflags}
%endif
%install
make install DESTDIR=$RPM_BUILD_ROOT
%global build_archlib $RPM_BUILD_ROOT%{archlib}
%global build_privlib $RPM_BUILD_ROOT%{privlib}
%global build_bindir  $RPM_BUILD_ROOT%{_bindir}
%global new_perl LD_PRELOAD="%{build_archlib}/CORE/libperl.so" \\\
    LD_LIBRARY_PATH="%{build_archlib}/CORE" \\\
    PERL5LIB="%{build_archlib}:%{build_privlib}" \\\
    %{build_bindir}/perl
mv "%{build_archlib}/CORE/libperl.so" \
    "$RPM_BUILD_ROOT%{_libdir}/libperl.so.%{perl_version}"
ln -s "libperl.so.%{perl_version}" "$RPM_BUILD_ROOT%{_libdir}/%{soname}"
ln -s "libperl.so.%{perl_version}" "$RPM_BUILD_ROOT%{_libdir}/libperl.so"
ln -s "../../libperl.so.%{perl_version}" "%{build_archlib}/CORE/libperl.so"
rm -f "%{build_archlib}/CORE/%{soname}"
install -p -m 755 utils/pl2pm %{build_bindir}/pl2pm
for i in sys/ioctl.h sys/syscall.h syscall.h
do
    %{new_perl} %{build_bindir}/h2ph -a -d %{build_archlib} $i || true
done
mkdir -p $RPM_BUILD_ROOT%{perl_vendorarch}/auto
mkdir -p $RPM_BUILD_ROOT%{perl_vendorlib}
mkdir -p ${RPM_BUILD_ROOT}%{_rpmmacrodir}
install -p -m 644 %{SOURCE3} ${RPM_BUILD_ROOT}%{_rpmmacrodir}
find $RPM_BUILD_ROOT -type f -name '*.bs' -empty -delete
chmod -R u+w $RPM_BUILD_ROOT/*
rm %{build_privlib}/ExtUtils/xsubpp
ln -s ../../../bin/xsubpp %{build_privlib}/ExtUtils/
rm %{build_archlib}/.packlist
rm %{build_archlib}/File/Spec/VMS.pm
rm $RPM_BUILD_ROOT%{_mandir}/man3/File::Spec::VMS.3*
rm %{build_privlib}/ExtUtils/PL2Bat.pm
rm $RPM_BUILD_ROOT%{_mandir}/man3/ExtUtils::PL2Bat.3*
mkdir -p %{buildroot}%{perl5_testdir}/perl-tests
tar -cf - t/ | ( cd %{buildroot}%{perl5_testdir}/perl-tests && tar -xf - )
for dir in `find ext/ -type d -name t -maxdepth 2` ; do
    tar -cf - $dir | ( cd %{buildroot}%{perl5_testdir}/perl-tests/t && tar -xf - )
done
%{new_perl} -MConfig -i -pn \
    -e 's"\A#!(?:perl|\./perl|/perl|/usr/bin/perl|/usr/bin/env perl)\b"$Config{startperl}"' \
    $(find %{buildroot}%{perl5_testdir}/perl-tests -type f)
%if %{with perl_enables_systemtap}
mkdir -p %{buildroot}%{tapsetdir}
%ifarch %{multilib_64_archs}
%global libperl_stp libperl%{perl_version}-64.stp
%else
%global libperl_stp libperl%{perl_version}-32.stp
%endif
sed \
  -e "s|LIBRARY_PATH|%{_libdir}/%{soname}|" \
  %{SOURCE4} \
  > %{buildroot}%{tapsetdir}/%{libperl_stp}
%endif
%if ! %{dual_life} && ! %{rebuild_from_scratch}
rm %{buildroot}%{_bindir}/ptar
rm %{buildroot}%{_bindir}/ptardiff
rm %{buildroot}%{_bindir}/ptargrep
rm -rf %{buildroot}%{privlib}/Archive/Tar
rm %{buildroot}%{privlib}/Archive/Tar.pm
rm -rf %{buildroot}%{privlib}/Archive
rm %{buildroot}%{_mandir}/man1/ptar.1*
rm %{buildroot}%{_mandir}/man1/ptardiff.1*
rm %{buildroot}%{_mandir}/man1/ptargrep.1*
rm %{buildroot}%{_mandir}/man3/Archive::Tar*
rm -rf %{buildroot}%{privlib}/autodie/
rm %{buildroot}%{privlib}/autodie.pm
rm %{buildroot}%{privlib}/Fatal.pm
rm %{buildroot}%{_mandir}/man3/autodie.3*
rm %{buildroot}%{_mandir}/man3/autodie::*
rm %{buildroot}%{_mandir}/man3/Fatal.3*
rm %{buildroot}%{privlib}/bigfloat.pm
rm %{buildroot}%{privlib}/bigint.pm
rm %{buildroot}%{privlib}/bignum.pm
rm %{buildroot}%{privlib}/bigrat.pm
rm -rf %{buildroot}%{privlib}/Math/BigFloat
rm %{buildroot}%{privlib}/Math/BigInt/Trace.pm
rm %{buildroot}%{privlib}/Math/BigRat/Trace.pm
rm -rf %{buildroot}%{privlib}/Math/BigRat
rm %{buildroot}%{_mandir}/man3/bigfloat.*
rm %{buildroot}%{_mandir}/man3/bigint.*
rm %{buildroot}%{_mandir}/man3/bignum.*
rm %{buildroot}%{_mandir}/man3/bigrat.*
rm -rf %{buildroot}%{privlib}/Carp
rm %{buildroot}%{privlib}/Carp.*
rm %{buildroot}%{_mandir}/man3/Carp.*
rm %{buildroot}%{archlib}/Compress/Raw/Bzip2.pm
rm -rf %{buildroot}%{archlib}/auto/Compress/Raw/Bzip2
rm %{buildroot}%{_mandir}/man3/Compress::Raw::Bzip2*
rm %{buildroot}%{archlib}/Compress/Raw/Zlib.pm
rm -rf %{buildroot}%{archlib}/Compress/Raw
rm -rf %{buildroot}%{archlib}/Compress
rm -rf %{buildroot}%{archlib}/auto/Compress/Raw/Zlib
rm -rf %{buildroot}%{archlib}/auto/Compress/Raw
rm -rf %{buildroot}%{archlib}/auto/Compress
rm %{buildroot}%{_mandir}/man3/Compress::Raw::Zlib*
rm -rf %{buildroot}%{privlib}/Config/Perl
rm %{buildroot}%{_mandir}/man3/Config::Perl::V.*
rm %{buildroot}%{privlib}/constant.pm
rm %{buildroot}%{_mandir}/man3/constant.3*
rm -rf %{buildroot}%{privlib}/CPAN/Meta/Requirements
rm %{buildroot}%{privlib}/CPAN/Meta/Requirements.pm
rm %{buildroot}%{_mandir}/man3/CPAN::Meta::Requirements*
rm %{buildroot}%{privlib}/CPAN/Meta/YAML.pm
rm %{buildroot}%{_mandir}/man3/CPAN::Meta::YAML*
rm %{buildroot}%{privlib}/CPAN/Meta.pm
rm %{buildroot}%{privlib}/CPAN/Meta/Converter.pm
rm %{buildroot}%{privlib}/CPAN/Meta/Feature.pm
rm -rf %{buildroot}%{privlib}/CPAN/Meta/History
rm %{buildroot}%{privlib}/CPAN/Meta/History.pm
rm %{buildroot}%{privlib}/CPAN/Meta/Merge.pm
rm %{buildroot}%{privlib}/CPAN/Meta/Prereqs.pm
rm %{buildroot}%{privlib}/CPAN/Meta/Spec.pm
rm %{buildroot}%{privlib}/CPAN/Meta/Validator.pm
rm -rf %{buildroot}%{privlib}/CPAN/Meta
rm %{buildroot}%{privlib}/Parse/CPAN/Meta.pm
rm -rf %{buildroot}%{privlib}/Parse/CPAN
rm -rf %{buildroot}%{privlib}/Parse
rm %{buildroot}%{_mandir}/man3/CPAN::Meta*
rm %{buildroot}%{_mandir}/man3/Parse::CPAN::Meta.3*
rm %{buildroot}%{_bindir}/cpan
rm %{buildroot}%{privlib}/App/Cpan.pm
rm -rf %{buildroot}%{privlib}/CPAN
rm %{buildroot}%{privlib}/CPAN.pm
rm %{buildroot}%{_mandir}/man1/cpan.1*
rm %{buildroot}%{_mandir}/man3/App::Cpan.*
rm %{buildroot}%{_mandir}/man3/CPAN.*
rm %{buildroot}%{_mandir}/man3/CPAN:*
rm %{buildroot}%{archlib}/auto/Data/Dumper/Dumper.so
rm %{buildroot}%{archlib}/Data/Dumper.pm
rm -rf %{buildroot}%{archlib}/auto/Data/Dumper
rm -rf %{buildroot}%{archlib}/auto/Data
rm -rf %{buildroot}%{archlib}/Data
rm %{buildroot}%{_mandir}/man3/Data::Dumper.3*
%if %{with bdb}
rm %{buildroot}%{archlib}/DB_File.pm
rm %{buildroot}%{archlib}/auto/DB_File/DB_File.so
rm -rf %{buildroot}%{archlib}/auto/DB_File
rm %{buildroot}%{_mandir}/man3/DB_File*
%endif
rm %{buildroot}%{archlib}/Devel/PPPort.pm
rm %{buildroot}%{_mandir}/man3/Devel::PPPort.3*
rm %{buildroot}%{privlib}/Digest.pm
rm %{buildroot}%{privlib}/Digest/base.pm
rm %{buildroot}%{privlib}/Digest/file.pm
rm -rf %{buildroot}%{privlib}/Digest
rm %{buildroot}%{_mandir}/man3/Digest.3*
rm %{buildroot}%{_mandir}/man3/Digest::base.3*
rm %{buildroot}%{_mandir}/man3/Digest::file.3*
rm %{buildroot}%{archlib}/Digest/MD5.pm
rm -rf %{buildroot}%{archlib}/auto/Digest/MD5
rm %{buildroot}%{_mandir}/man3/Digest::MD5.3*
rm %{buildroot}%{_bindir}/shasum
rm %{buildroot}%{archlib}/Digest/SHA.pm
rm -rf %{buildroot}%{archlib}/Digest
rm -rf %{buildroot}%{archlib}/auto/Digest/SHA
rm -rf %{buildroot}%{archlib}/auto/Digest
rm %{buildroot}%{_mandir}/man1/shasum.1*
rm %{buildroot}%{_mandir}/man3/Digest::SHA.3*
rm %{buildroot}%{_bindir}/encguess
rm %{buildroot}%{_bindir}/piconv
rm -rf %{buildroot}%{archlib}/Encode*
rm -rf %{buildroot}%{archlib}/auto/Encode*
rm %{buildroot}%{_mandir}/man1/encguess.1*
rm %{buildroot}%{_mandir}/man1/piconv.1*
rm %{buildroot}%{_mandir}/man3/Encode*.3*
rm %{buildroot}%{archlib}/encoding.pm
rm %{buildroot}%{_mandir}/man3/encoding.3*
rm %{buildroot}%{_bindir}/enc2xs
rm %{buildroot}%{privlib}/Encode/*.e2x
rm %{buildroot}%{privlib}/Encode/encode.h
rm -rf %{buildroot}%{privlib}/Encode
rm %{buildroot}%{_mandir}/man1/enc2xs.1*
rm %{buildroot}%{privlib}/Env.pm
rm %{buildroot}%{_mandir}/man3/Env.3*
rm -rf %{buildroot}%{privlib}/Exporter*
rm %{buildroot}%{_mandir}/man3/Exporter*
rm %{buildroot}%{privlib}/experimental*
rm %{buildroot}%{privlib}/stable*
rm %{buildroot}%{_mandir}/man3/experimental*
rm %{buildroot}%{_mandir}/man3/stable*
rm %{buildroot}%{privlib}/ExtUtils/CBuilder.pm
rm -rf %{buildroot}%{privlib}/ExtUtils/CBuilder
rm %{buildroot}%{_mandir}/man3/ExtUtils::CBuilder*
rm %{buildroot}%{privlib}/ExtUtils/Command.pm
rm %{buildroot}%{_mandir}/man3/ExtUtils::Command.*
rm %{buildroot}%{privlib}/ExtUtils/Install.pm
rm %{buildroot}%{privlib}/ExtUtils/Installed.pm
rm %{buildroot}%{privlib}/ExtUtils/Packlist.pm
rm %{buildroot}%{_mandir}/man3/ExtUtils::Install.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Installed.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Packlist.3*
rm %{buildroot}%{privlib}/ExtUtils/Manifest.pm
rm %{buildroot}%{privlib}/ExtUtils/MANIFEST.SKIP
rm %{buildroot}%{_mandir}/man3/ExtUtils::Manifest.3*
rm %{buildroot}%{_bindir}/instmodsh
rm -rf %{buildroot}%{privlib}/ExtUtils/Command
rm -rf %{buildroot}%{privlib}/ExtUtils/Liblist
rm %{buildroot}%{privlib}/ExtUtils/Liblist.pm
rm -rf %{buildroot}%{privlib}/ExtUtils/MakeMaker
rm %{buildroot}%{privlib}/ExtUtils/MakeMaker.pm
rm %{buildroot}%{privlib}/ExtUtils/MM.pm
rm %{buildroot}%{privlib}/ExtUtils/MM_*.pm
rm %{buildroot}%{privlib}/ExtUtils/MY.pm
rm %{buildroot}%{privlib}/ExtUtils/Mkbootstrap.pm
rm %{buildroot}%{privlib}/ExtUtils/Mksymlists.pm
rm %{buildroot}%{privlib}/ExtUtils/testlib.pm
rm %{buildroot}%{_mandir}/man1/instmodsh.1*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Command::MM*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Liblist.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::MM.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::MM_*
rm %{buildroot}%{_mandir}/man3/ExtUtils::MY.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::MakeMaker*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Mkbootstrap.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Mksymlists.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::testlib.3*
rm %{buildroot}%{privlib}/ExtUtils/MM/Utils.pm
rm -rf %{buildroot}%{privlib}/ExtUtils/MM
rm %{buildroot}%{_mandir}/man3/ExtUtils::MM::Utils.*
rm %{buildroot}%{privlib}/ExtUtils/ParseXS.pm
rm %{buildroot}%{privlib}/ExtUtils/ParseXS.pod
rm %{buildroot}%{privlib}/ExtUtils/ParseXS/Constants.pm
rm %{buildroot}%{privlib}/ExtUtils/ParseXS/CountLines.pm
rm %{buildroot}%{privlib}/ExtUtils/ParseXS/Eval.pm
rm %{buildroot}%{privlib}/ExtUtils/ParseXS/Node.pm
rm %{buildroot}%{privlib}/ExtUtils/ParseXS/Utilities.pm
rm -rf %{buildroot}%{privlib}/ExtUtils/ParseXS
rm %{buildroot}%{privlib}/ExtUtils/Typemaps.pm
rm %{buildroot}%{privlib}/ExtUtils/Typemaps/Cmd.pm
rm %{buildroot}%{privlib}/ExtUtils/Typemaps/InputMap.pm
rm %{buildroot}%{privlib}/ExtUtils/Typemaps/OutputMap.pm
rm %{buildroot}%{privlib}/ExtUtils/Typemaps/Type.pm
rm -rf %{buildroot}%{privlib}/ExtUtils/Typemaps
rm %{buildroot}%{privlib}/ExtUtils/xsubpp
rm %{buildroot}%{privlib}/pod/perlxs.pod
rm %{buildroot}%{privlib}/pod/perlxstut.pod
rm %{buildroot}%{privlib}/pod/perlxstypemap.pod
rm %{buildroot}%{_bindir}/xsubpp
rm %{buildroot}%{_mandir}/man1/perlxs*
rm %{buildroot}%{_mandir}/man1/xsubpp*
rm %{buildroot}%{_mandir}/man3/ExtUtils::ParseXS.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::ParseXS::Constants.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::ParseXS::Eval.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::ParseXS::Node.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::ParseXS::Utilities.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Typemaps.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Typemaps::Cmd.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Typemaps::InputMap.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Typemaps::OutputMap.3*
rm %{buildroot}%{_mandir}/man3/ExtUtils::Typemaps::Type.3*
rm %{buildroot}%{privlib}/File/Fetch.pm
rm %{buildroot}%{_mandir}/man3/File::Fetch.3*
rm %{buildroot}%{privlib}/File/Path.pm
rm %{buildroot}%{_mandir}/man3/File::Path.3*
rm %{buildroot}%{privlib}/File/Temp.pm
rm %{buildroot}%{_mandir}/man3/File::Temp.3*
rm -rf %{buildroot}%{archlib}/auto/Filter/Util
rm -rf %{buildroot}%{archlib}/auto/Filter
rm -rf %{buildroot}%{archlib}/Filter/Util
rm -rf %{buildroot}%{archlib}/Filter
rm %{buildroot}%{privlib}/pod/perlfilter.pod
rm %{buildroot}%{_mandir}/man1/perlfilter.*
rm %{buildroot}%{_mandir}/man3/Filter::Util::*
rm %{buildroot}%{privlib}/Filter/Simple.pm
rm -rf %{buildroot}%{privlib}/Filter
rm %{buildroot}%{_mandir}/man3/Filter::Simple.3*
rm %{buildroot}%{privlib}/Getopt/Long.pm
rm %{buildroot}%{privlib}/Getopt/Long/Parser.pm
rm %{buildroot}%{_mandir}/man3/Getopt::Long.3*
rm %{buildroot}%{_mandir}/man3/Getopt::Long::Parser.3*
rm %{buildroot}%{_bindir}/streamzip
rm %{buildroot}%{_bindir}/zipdetails
rm %{buildroot}%{privlib}/IO/Compress.pm
rm %{buildroot}%{privlib}/IO/Compress/FAQ.pod
rm %{buildroot}%{_mandir}/man1/streamzip.*
rm %{buildroot}%{_mandir}/man1/zipdetails.*
rm %{buildroot}%{_mandir}/man3/IO::Compress.3*
rm %{buildroot}%{_mandir}/man3/IO::Compress::FAQ.*
rm %{buildroot}%{privlib}/Compress/Zlib.pm
rm -rf %{buildroot}%{privlib}/Compress
rm %{buildroot}%{_mandir}/man3/Compress::Zlib*
rm %{buildroot}%{privlib}/File/GlobMapper.pm
rm %{buildroot}%{privlib}/IO/Compress/Base.pm
rm -rf %{buildroot}%{privlib}/IO/Compress/Base
rm %{buildroot}%{privlib}/IO/Uncompress/AnyUncompress.pm
rm %{buildroot}%{privlib}/IO/Uncompress/Base.pm
rm %{buildroot}%{_mandir}/man3/File::GlobMapper.*
rm %{buildroot}%{_mandir}/man3/IO::Compress::Base.*
rm %{buildroot}%{_mandir}/man3/IO::Uncompress::AnyUncompress.*
rm %{buildroot}%{_mandir}/man3/IO::Uncompress::Base.*
rm %{buildroot}%{privlib}/IO/Compress/Bzip2.pm
rm %{buildroot}%{privlib}/IO/Compress/Deflate.pm
rm %{buildroot}%{privlib}/IO/Compress/Gzip.pm
rm %{buildroot}%{privlib}/IO/Compress/RawDeflate.pm
rm %{buildroot}%{privlib}/IO/Compress/Zip.pm
rm -rf %{buildroot}%{privlib}/IO/Compress/Adapter
rm -rf %{buildroot}%{privlib}/IO/Compress/Gzip
rm -rf %{buildroot}%{privlib}/IO/Compress/Zip
rm -rf %{buildroot}%{privlib}/IO/Compress/Zlib
rm -rf %{buildroot}%{privlib}/IO/Compress
rm %{buildroot}%{privlib}/IO/Uncompress/AnyInflate.pm
rm %{buildroot}%{privlib}/IO/Uncompress/Bunzip2.pm
rm %{buildroot}%{privlib}/IO/Uncompress/Gunzip.pm
rm %{buildroot}%{privlib}/IO/Uncompress/Inflate.pm
rm %{buildroot}%{privlib}/IO/Uncompress/RawInflate.pm
rm %{buildroot}%{privlib}/IO/Uncompress/Unzip.pm
rm -rf %{buildroot}%{privlib}/IO/Uncompress/Adapter
rm -rf %{buildroot}%{privlib}/IO/Uncompress
rm %{buildroot}%{_mandir}/man3/IO::Compress::Deflate*
rm %{buildroot}%{_mandir}/man3/IO::Compress::Bzip2*
rm %{buildroot}%{_mandir}/man3/IO::Compress::Gzip*
rm %{buildroot}%{_mandir}/man3/IO::Compress::RawDeflate*
rm %{buildroot}%{_mandir}/man3/IO::Compress::Zip*
rm %{buildroot}%{_mandir}/man3/IO::Uncompress::AnyInflate*
rm %{buildroot}%{_mandir}/man3/IO::Uncompress::Bunzip2*
rm %{buildroot}%{_mandir}/man3/IO::Uncompress::Gunzip*
rm %{buildroot}%{_mandir}/man3/IO::Uncompress::Inflate*
rm %{buildroot}%{_mandir}/man3/IO::Uncompress::RawInflate*
rm %{buildroot}%{_mandir}/man3/IO::Uncompress::Unzip*
rm %{buildroot}%{privlib}/IO/Socket/IP.pm
rm -rf %{buildroot}%{privlib}/IO/Socket
rm %{buildroot}%{_mandir}/man3/IO::Socket::IP.*
rm %{buildroot}%{privlib}/IO/Zlib.pm
rm -rf %{buildroot}%{privlib}/IO
rm %{buildroot}%{_mandir}/man3/IO::Zlib.*
rm %{buildroot}%{privlib}/HTTP/Tiny.pm
rm -rf %{buildroot}%{privlib}/HTTP
rm %{buildroot}%{_mandir}/man3/HTTP::Tiny*
rm %{buildroot}%{privlib}/IPC/Cmd.pm
rm %{buildroot}%{_mandir}/man3/IPC::Cmd.3*
rm -rf %{buildroot}%{archlib}/auto/IPC
rm %{buildroot}%{archlib}/IPC/Msg.pm
rm %{buildroot}%{archlib}/IPC/Semaphore.pm
rm %{buildroot}%{archlib}/IPC/SharedMem.pm
rm %{buildroot}%{archlib}/IPC/SysV.pm
rm -rf %{buildroot}%{archlib}/IPC
rm %{buildroot}%{_mandir}/man3/IPC::Msg.*
rm %{buildroot}%{_mandir}/man3/IPC::Semaphore.*
rm %{buildroot}%{_mandir}/man3/IPC::SharedMem.*
rm %{buildroot}%{_mandir}/man3/IPC::SysV.*
rm %{buildroot}%{_bindir}/json_pp
rm %{buildroot}%{privlib}/JSON/PP.pm
rm -rf %{buildroot}%{privlib}/JSON/PP
rm -rf %{buildroot}%{privlib}/JSON
rm %{buildroot}%{_mandir}/man1/json_pp.1*
rm %{buildroot}%{_mandir}/man3/JSON::PP.3*
rm %{buildroot}%{_mandir}/man3/JSON::PP::Boolean.3pm*
rm %{buildroot}%{privlib}/Net/Cmd.pm
rm %{buildroot}%{privlib}/Net/Config.pm
rm %{buildroot}%{privlib}/Net/Domain.pm
rm %{buildroot}%{privlib}/Net/FTP.pm
rm -rf %{buildroot}%{privlib}/Net/FTP
rm %{buildroot}%{privlib}/Net/libnetFAQ.pod
rm %{buildroot}%{privlib}/Net/NNTP.pm
rm %{buildroot}%{privlib}/Net/Netrc.pm
rm %{buildroot}%{privlib}/Net/POP3.pm
rm %{buildroot}%{privlib}/Net/SMTP.pm
rm %{buildroot}%{privlib}/Net/Time.pm
rm %{buildroot}%{_mandir}/man3/Net::Cmd.*
rm %{buildroot}%{_mandir}/man3/Net::Config.*
rm %{buildroot}%{_mandir}/man3/Net::Domain.*
rm %{buildroot}%{_mandir}/man3/Net::FTP.*
rm %{buildroot}%{_mandir}/man3/Net::libnetFAQ.*
rm %{buildroot}%{_mandir}/man3/Net::NNTP.*
rm %{buildroot}%{_mandir}/man3/Net::Netrc.*
rm %{buildroot}%{_mandir}/man3/Net::POP3.*
rm %{buildroot}%{_mandir}/man3/Net::SMTP.*
rm %{buildroot}%{_mandir}/man3/Net::Time.*
rm %{buildroot}%{privlib}/Locale/Maketext.*
rm %{buildroot}%{privlib}/Locale/Maketext/Cookbook.*
rm %{buildroot}%{privlib}/Locale/Maketext/Guts.*
rm %{buildroot}%{privlib}/Locale/Maketext/GutsLoader.*
rm %{buildroot}%{privlib}/Locale/Maketext/TPJ13.*
rm %{buildroot}%{_mandir}/man3/Locale::Maketext.*
rm %{buildroot}%{_mandir}/man3/Locale::Maketext::Cookbook.*
rm %{buildroot}%{_mandir}/man3/Locale::Maketext::Guts.*
rm %{buildroot}%{_mandir}/man3/Locale::Maketext::GutsLoader.*
rm %{buildroot}%{_mandir}/man3/Locale::Maketext::TPJ13.*
rm %{buildroot}%{privlib}/Math/BigFloat.pm
rm %{buildroot}%{privlib}/Math/BigInt.pm
rm %{buildroot}%{privlib}/Math/BigInt/Calc.pm
rm %{buildroot}%{privlib}/Math/BigInt/Lib.pm
rm %{buildroot}%{privlib}/Math/BigRat.pm
rm -rf %{buildroot}%{privlib}/Math/BigInt
rm %{buildroot}%{_mandir}/man3/Math::BigFloat.*
rm %{buildroot}%{_mandir}/man3/Math::BigInt.*
rm %{buildroot}%{_mandir}/man3/Math::BigInt::Calc.*
rm %{buildroot}%{_mandir}/man3/Math::BigInt::Lib.*
rm %{buildroot}%{_mandir}/man3/Math::BigRat.*
rm -rf %{buildroot}%{archlib}/Math
rm -rf %{buildroot}%{archlib}/auto/Math
rm %{buildroot}%{_mandir}/man3/Math::BigInt::FastCalc.*
rm -rf %{buildroot}%{archlib}/auto/MIME
rm -rf %{buildroot}%{archlib}/MIME
rm %{buildroot}%{_mandir}/man3/MIME::*
rm -rf %{buildroot}%{privlib}/Module/CoreList
rm %{buildroot}%{privlib}/Module/CoreList.pm
rm %{buildroot}%{privlib}/Module/CoreList.pod
rm %{buildroot}%{_mandir}/man3/Module::CoreList*
rm %{buildroot}%{_bindir}/corelist
rm %{buildroot}%{_mandir}/man1/corelist*
rm %{buildroot}%{privlib}/Module/Load.pm
rm %{buildroot}%{_mandir}/man3/Module::Load.*
rm -rf %{buildroot}%{privlib}/Module/Load
rm %{buildroot}%{_mandir}/man3/Module::Load::Conditional*
rm %{buildroot}%{privlib}/Module/Metadata.pm
rm %{buildroot}%{_mandir}/man3/Module::Metadata.3pm*
rm %{buildroot}%{privlib}/Net/Ping.pm
rm %{buildroot}%{_mandir}/man3/Net::Ping.*
rm %{buildroot}%{privlib}/parent.pm
rm %{buildroot}%{_mandir}/man3/parent.3*
rm -rf %{buildroot}%{privlib}/Params/
rm %{buildroot}%{_mandir}/man3/Params::Check*
rm %{buildroot}%{archlib}/Cwd.pm
rm -rf %{buildroot}%{archlib}/File/Spec*
rm -rf %{buildroot}%{archlib}/auto/Cwd/
rm %{buildroot}%{_mandir}/man3/Cwd*
rm %{buildroot}%{_mandir}/man3/File::Spec*
rm %{buildroot}%{privlib}/Perl/OSType.pm
rm -rf %{buildroot}%{privlib}/Perl
rm %{buildroot}%{_mandir}/man3/Perl::OSType.3pm*
rm %{buildroot}%{privlib}/perlfaq.pm
rm %{buildroot}%{privlib}/pod/perlfaq*
rm %{buildroot}%{privlib}/pod/perlglossary.pod
rm %{buildroot}%{_mandir}/man1/perlfaq*
rm %{buildroot}%{_mandir}/man1/perlglossary.*
rm -rf %{buildroot}%{privlib}/PerlIO/via
rm %{buildroot}%{_mandir}/man3/PerlIO::via::QuotedPrint.*
rm %{buildroot}%{_bindir}/podchecker
rm %{buildroot}%{privlib}/Pod/Checker.pm
rm %{buildroot}%{_mandir}/man1/podchecker.*
rm %{buildroot}%{_mandir}/man3/Pod::Checker.*
rm %{buildroot}%{privlib}/Pod/Escapes.pm
rm %{buildroot}%{_mandir}/man3/Pod::Escapes.*
rm %{buildroot}%{_bindir}/perldoc
rm %{buildroot}%{privlib}/pod/perldoc.pod
rm %{buildroot}%{privlib}/Pod/Perldoc.pm
rm -rf %{buildroot}%{privlib}/Pod/Perldoc/
rm %{buildroot}%{_mandir}/man1/perldoc.1*
rm %{buildroot}%{_mandir}/man3/Pod::Perldoc*
rm %{buildroot}%{_bindir}/pod2usage
rm %{buildroot}%{privlib}/Pod/Usage.pm
rm %{buildroot}%{_mandir}/man1/pod2usage.*
rm %{buildroot}%{_mandir}/man3/Pod::Usage.*
rm %{buildroot}%{_bindir}/pod2man
rm %{buildroot}%{_bindir}/pod2text
rm %{buildroot}%{privlib}/pod/perlpodstyle.pod
rm %{buildroot}%{privlib}/Pod/Man.pm
rm %{buildroot}%{privlib}/Pod/ParseLink.pm
rm %{buildroot}%{privlib}/Pod/Text.pm
rm -rf %{buildroot}%{privlib}/Pod/Text
rm %{buildroot}%{_mandir}/man1/pod2man.1*
rm %{buildroot}%{_mandir}/man1/pod2text.1*
rm %{buildroot}%{_mandir}/man1/perlpodstyle.1*
rm %{buildroot}%{_mandir}/man3/Pod::Man*
rm %{buildroot}%{_mandir}/man3/Pod::ParseLink*
rm %{buildroot}%{_mandir}/man3/Pod::Text*
rm %{buildroot}%{privlib}/Pod/Simple.pm
rm %{buildroot}%{privlib}/Pod/Simple.pod
rm -rf %{buildroot}%{privlib}/Pod/Simple/
rm %{buildroot}%{_mandir}/man3/Pod::Simple*
rm -rf %{buildroot}%{archlib}/List/
rm -rf %{buildroot}%{archlib}/Scalar/
rm -rf %{buildroot}%{archlib}/Sub/
rm -rf %{buildroot}%{archlib}/auto/List/
rm %{buildroot}%{_mandir}/man3/List::Util*
rm %{buildroot}%{_mandir}/man3/Scalar::Util*
rm %{buildroot}%{_mandir}/man3/Scalar::List::Utils*
rm %{buildroot}%{_mandir}/man3/Sub::Util*
rm %{buildroot}%{archlib}/auto/Socket/Socket.*
rm -rf %{buildroot}%{archlib}/auto/Socket
rm %{buildroot}%{archlib}/Socket.pm
rm %{buildroot}%{_mandir}/man3/Socket.3*
rm %{buildroot}%{archlib}/Storable.pm
rm -rf %{buildroot}%{archlib}/auto/Storable/
rm %{buildroot}%{_mandir}/man3/Storable.*
rm %{buildroot}%{archlib}/Sys/Syslog.pm
rm -rf %{buildroot}%{archlib}/auto/Sys/Syslog/
rm %{buildroot}%{_mandir}/man3/Sys::Syslog.*
rm %{buildroot}%{privlib}/Term/ANSIColor.pm
rm %{buildroot}%{_mandir}/man3/Term::ANSIColor*
rm %{buildroot}%{privlib}/Term/Cap.pm
rm %{buildroot}%{_mandir}/man3/Term::Cap.*
rm %{buildroot}%{privlib}/Term/Table.pm
rm %{buildroot}%{privlib}/Term/Table//Cell.pm
rm %{buildroot}%{privlib}/Term/Table/CellStack.pm
rm %{buildroot}%{privlib}/Term/Table/HashBase.pm
rm %{buildroot}%{privlib}/Term/Table/LineBreak.pm
rm %{buildroot}%{privlib}/Term/Table/Spacer.pm
rm %{buildroot}%{privlib}/Term/Table/Util.pm
rm %{buildroot}%{_mandir}/man3/Term::Table*
rm %{buildroot}%{_bindir}/prove
rm -rf %{buildroot}%{privlib}/App/Prove*
rm -rf %{buildroot}%{privlib}/App
rm -rf %{buildroot}%{privlib}/TAP*
rm %{buildroot}%{privlib}/Test/Harness*
rm %{buildroot}%{_mandir}/man1/prove.1*
rm %{buildroot}%{_mandir}/man3/App::Prove*
rm %{buildroot}%{_mandir}/man3/TAP*
rm %{buildroot}%{_mandir}/man3/Test::Harness*
rm %{buildroot}%{privlib}/ok*
rm %{buildroot}%{privlib}/Test/More*
rm -rf %{buildroot}%{privlib}/Test/Builder*
rm -rf %{buildroot}%{privlib}/Test/Tester*
rm %{buildroot}%{privlib}/Test/Simple*
rm %{buildroot}%{privlib}/Test/Tutorial*
rm -rf %{buildroot}%{privlib}/Test/use
rm -rf %{buildroot}%{privlib}/Test
rm -rf %{buildroot}%{privlib}/Test2.pm
rm -rf %{buildroot}%{privlib}/Test2/API*
rm -rf %{buildroot}%{privlib}/Test2/Event.pm
rm -rf %{buildroot}%{privlib}/Test2/Event/*
rm -rf %{buildroot}%{privlib}/Test2/EventFacet*
rm -rf %{buildroot}%{privlib}/Test2/Formatter*
rm -rf %{buildroot}%{privlib}/Test2/Hub*
rm -rf %{buildroot}%{privlib}/Test2/IPC*
rm -rf %{buildroot}%{privlib}/Test2/Tools/Tiny.pm
rm -rf %{buildroot}%{privlib}/Test2/Transition.pod
rm %{buildroot}%{privlib}/Test2/Env.pm
rm %{buildroot}%{privlib}/Test2/Util.pm
rm %{buildroot}%{privlib}/Test2/Util/ExternalMeta.pm
rm %{buildroot}%{privlib}/Test2/Util/Facets2Legacy.pm
rm %{buildroot}%{privlib}/Test2/Util/HashBase.pm
rm %{buildroot}%{privlib}/Test2/Util/Sig.pm
rm %{buildroot}%{privlib}/Test2/Util/Trace.pm
rm %{buildroot}%{_mandir}/man3/ok*
rm %{buildroot}%{_mandir}/man3/Test::More*
rm %{buildroot}%{_mandir}/man3/Test::Builder*
rm %{buildroot}%{_mandir}/man3/Test::Tester*
rm %{buildroot}%{_mandir}/man3/Test::Simple*
rm %{buildroot}%{_mandir}/man3/Test::Tutorial*
rm %{buildroot}%{_mandir}/man3/Test::use::*
rm %{buildroot}%{_mandir}/man3/Test2.*
rm %{buildroot}%{_mandir}/man3/Test2::API*
rm %{buildroot}%{_mandir}/man3/Test2::Env.*
rm %{buildroot}%{_mandir}/man3/Test2::Event.*
rm %{buildroot}%{_mandir}/man3/Test2::Event::*
rm %{buildroot}%{_mandir}/man3/Test2::EventFacet*
rm %{buildroot}%{_mandir}/man3/Test2::Formatter*
rm %{buildroot}%{_mandir}/man3/Test2::Hub*
rm %{buildroot}%{_mandir}/man3/Test2::IPC*
rm %{buildroot}%{_mandir}/man3/Test2::Tools::Tiny*
rm %{buildroot}%{_mandir}/man3/Test2::Transition*
rm %{buildroot}%{_mandir}/man3/Test2::Util.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::ExternalMeta.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Facets2Legacy.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::HashBase.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Sig.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Trace.*
rm -rf %{buildroot}%{privlib}/Test2/AsyncSubtest*
rm -rf %{buildroot}%{privlib}/Test2/Bundle*
rm -rf %{buildroot}%{privlib}/Test2/Compare*
rm -rf %{buildroot}%{privlib}/Test2/Manual*
rm %{buildroot}%{privlib}/Test2/Mock.pm
rm -rf %{buildroot}%{privlib}/Test2/Plugin*
rm -rf %{buildroot}%{privlib}/Test2/Require*
rm %{buildroot}%{privlib}/Test2/Suite.pm
rm %{buildroot}%{privlib}/Test2/Todo.pm
rm %{buildroot}%{privlib}/Test2/Tools.pm
rm -rf %{buildroot}%{privlib}/Test2/Tools
rm %{buildroot}%{privlib}/Test2/Util/Grabber.pm
rm %{buildroot}%{privlib}/Test2/Util/Guard.pm
rm %{buildroot}%{privlib}/Test2/Util/Importer.pm
rm %{buildroot}%{privlib}/Test2/Util/Ref.pm
rm %{buildroot}%{privlib}/Test2/Util/Stash.pm
rm %{buildroot}%{privlib}/Test2/Util/Sub.pm
rm -rf %{buildroot}%{privlib}/Test2/Util/Table
rm %{buildroot}%{privlib}/Test2/Util/Table.pm
rm %{buildroot}%{privlib}/Test2/Util/Term.pm
rm %{buildroot}%{privlib}/Test2/Util/Times.pm
rm -rf %{buildroot}%{privlib}/Test2/Util
rm %{buildroot}%{privlib}/Test2/V0.pm
rm -rf %{buildroot}%{privlib}/Test2/Workflow*
rm %{buildroot}%{_mandir}/man3/Test2::AsyncSubtest*
rm %{buildroot}%{_mandir}/man3/Test2::Bundle*
rm %{buildroot}%{_mandir}/man3/Test2::Compare*
rm %{buildroot}%{_mandir}/man3/Test2::Manual*
rm %{buildroot}%{_mandir}/man3/Test2::Mock.*
rm %{buildroot}%{_mandir}/man3/Test2::Plugin*
rm %{buildroot}%{_mandir}/man3/Test2::Require*
rm %{buildroot}%{_mandir}/man3/Test2::Suite.*
rm %{buildroot}%{_mandir}/man3/Test2::Todo.*
rm %{buildroot}%{_mandir}/man3/Test2::Tools.*
rm %{buildroot}%{_mandir}/man3/Test2::Tools::*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Grabber.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Guard.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Importer.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Ref.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Stash.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Sub.*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Table*
rm %{buildroot}%{_mandir}/man3/Test2::Util::Times.*
rm %{buildroot}%{_mandir}/man3/Test2::V0.*
rm %{buildroot}%{_mandir}/man3/Test2::Workflow*
rm %{buildroot}%{privlib}/Text/Balanced.pm
rm %{buildroot}%{_mandir}/man3/Text::Balanced.*
rm %{buildroot}%{privlib}/Text/ParseWords.pm
rm %{buildroot}%{_mandir}/man3/Text::ParseWords.*
rm %{buildroot}%{privlib}/Text/Tabs.pm
rm %{buildroot}%{privlib}/Text/Wrap.pm
rm %{buildroot}%{_mandir}/man3/Text::Tabs.*
rm %{buildroot}%{_mandir}/man3/Text::Wrap.*
rm %{buildroot}%{privlib}/Thread/Queue.pm
rm %{buildroot}%{_mandir}/man3/Thread::Queue.*
rm %{buildroot}%{privlib}/Tie/RefHash.pm
rm %{buildroot}%{_mandir}/man3/Tie::RefHash.*
rm %{buildroot}%{archlib}/Time/HiRes.pm
rm -rf %{buildroot}%{archlib}/auto/Time/HiRes
rm %{buildroot}%{_mandir}/man3/Time::HiRes.*
rm %{buildroot}%{privlib}/Time/Local.pm
rm %{buildroot}%{_mandir}/man3/Time::Local.*
rm %{buildroot}%{archlib}/auto/threads/threads*
rm %{buildroot}%{archlib}/threads.pm
rm %{buildroot}%{_mandir}/man3/threads.3*
rm -rf %{buildroot}%{archlib}/auto/threads/shared*
rm -rf %{buildroot}%{archlib}/auto/threads
rm %{buildroot}%{archlib}/threads/shared*
rm -rf %{buildroot}%{archlib}/threads
rm %{buildroot}%{_mandir}/man3/threads::shared*
rm -rf %{buildroot}%{archlib}/auto/Unicode/Collate
rm -rf %{buildroot}%{archlib}/auto/Unicode
rm %{buildroot}%{archlib}/Unicode/Collate.pm
rm -rf %{buildroot}%{archlib}/Unicode/Collate
rm -rf %{buildroot}%{privlib}/Unicode/Collate
rm %{buildroot}%{_mandir}/man3/Unicode::Collate.*
rm %{buildroot}%{_mandir}/man3/Unicode::Collate::*
rm -rf %{buildroot}%{archlib}/auto/Unicode/Normalize
rm %{buildroot}%{archlib}/Unicode/Normalize.pm
rm -rf %{buildroot}%{archlib}/Unicode
rm %{buildroot}%{_mandir}/man3/Unicode::Normalize.*
rm %{buildroot}%{privlib}/version.pm
rm %{buildroot}%{privlib}/version.pod
rm -rf %{buildroot}%{privlib}/version/
rm %{buildroot}%{_mandir}/man3/version.3*
rm %{buildroot}%{_mandir}/man3/version::Internals.3*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%check

%if %{with test}
%{new_perl} -Ilib -I/lib regen/lib_cleanup.pl
pushd t
%{new_perl} -I../lib porting/customized.t --regen
popd
    JOBS=$(printf '%%s' "%{?_smp_mflags}" | sed 's/.*-j\([0-9][0-9]*\).*/\1/')
    LC_ALL=C TEST_JOBS=$JOBS make test_harness
%endif
%if 0%{?flatpak}
mkdir -p %{buildroot}/usr/bin
ln -s /app/bin/perl %{buildroot}/usr/bin/perl
%endif
%ldconfig_scriptlets libs
%files -f %{oreon_filedir}/main.list
%files -n perl-interpreter -f %{oreon_filedir}/perl-interpreter.list
%files -n perl-libs -f %{oreon_filedir}/perl-libs.list
%files -n perl-devel -f %{oreon_filedir}/perl-devel.list
%files -n perl-macros -f %{oreon_filedir}/perl-macros.list
%files -n perl-tests -f %{oreon_filedir}/perl-tests.list
%files -n perl-utils -f %{oreon_filedir}/perl-utils.list
%files -n perl-Attribute-Handlers -f %{oreon_filedir}/perl-Attribute-Handlers.list
%files -n perl-AutoLoader -f %{oreon_filedir}/perl-AutoLoader.list
%files -n perl-AutoSplit -f %{oreon_filedir}/perl-AutoSplit.list
%files -n perl-autouse -f %{oreon_filedir}/perl-autouse.list
%files -n perl-B -f %{oreon_filedir}/perl-B.list
%files -n perl-base -f %{oreon_filedir}/perl-base.list
%files -n perl-Benchmark -f %{oreon_filedir}/perl-Benchmark.list
%files -n perl-blib -f %{oreon_filedir}/perl-blib.list
%files -n perl-Class-Struct -f %{oreon_filedir}/perl-Class-Struct.list
%files -n perl-Config-Extensions -f %{oreon_filedir}/perl-Config-Extensions.list
%files -n perl-DBM_Filter -f %{oreon_filedir}/perl-DBM_Filter.list
%files -n perl-debugger -f %{oreon_filedir}/perl-debugger.list
%files -n perl-deprecate -f %{oreon_filedir}/perl-deprecate.list
%files -n perl-Devel-Peek -f %{oreon_filedir}/perl-Devel-Peek.list
%files -n perl-Devel-SelfStubber -f %{oreon_filedir}/perl-Devel-SelfStubber.list
%files -n perl-diagnostics -f %{oreon_filedir}/perl-diagnostics.list
%files -n perl-DirHandle -f %{oreon_filedir}/perl-DirHandle.list
%files -n perl-doc -f %{oreon_filedir}/perl-doc.list
%files -n perl-Dumpvalue -f %{oreon_filedir}/perl-Dumpvalue.list
%files -n perl-DynaLoader -f %{oreon_filedir}/perl-DynaLoader.list
%files -n perl-encoding-warnings -f %{oreon_filedir}/perl-encoding-warnings.list
%files -n perl-English -f %{oreon_filedir}/perl-English.list
%files -n perl-Errno -f %{oreon_filedir}/perl-Errno.list
%files -n perl-ExtUtils-Constant -f %{oreon_filedir}/perl-ExtUtils-Constant.list
%files -n perl-ExtUtils-Embed -f %{oreon_filedir}/perl-ExtUtils-Embed.list
%files -n perl-ExtUtils-Miniperl -f %{oreon_filedir}/perl-ExtUtils-Miniperl.list
%files -n perl-Fcntl -f %{oreon_filedir}/perl-Fcntl.list
%files -n perl-fields -f %{oreon_filedir}/perl-fields.list
%files -n perl-File-Basename -f %{oreon_filedir}/perl-File-Basename.list
%files -n perl-File-Compare -f %{oreon_filedir}/perl-File-Compare.list
%files -n perl-File-Copy -f %{oreon_filedir}/perl-File-Copy.list
%files -n perl-File-DosGlob -f %{oreon_filedir}/perl-File-DosGlob.list
%files -n perl-File-Find -f %{oreon_filedir}/perl-File-Find.list
%files -n perl-File-stat -f %{oreon_filedir}/perl-File-stat.list
%files -n perl-FileCache -f %{oreon_filedir}/perl-FileCache.list
%files -n perl-FileHandle -f %{oreon_filedir}/perl-FileHandle.list
%files -n perl-filetest -f %{oreon_filedir}/perl-filetest.list
%files -n perl-FindBin -f %{oreon_filedir}/perl-FindBin.list
%files -n perl-GDBM_File -f %{oreon_filedir}/perl-GDBM_File.list
%files -n perl-Getopt-Std -f %{oreon_filedir}/perl-Getopt-Std.list
%files -n perl-Hash-Util -f %{oreon_filedir}/perl-Hash-Util.list
%files -n perl-Hash-Util-FieldHash -f %{oreon_filedir}/perl-Hash-Util-FieldHash.list
%files -n perl-if -f %{oreon_filedir}/perl-if.list
%files -n perl-IO -f %{oreon_filedir}/perl-IO.list
%files -n perl-IPC-Open3 -f %{oreon_filedir}/perl-IPC-Open3.list
%files -n perl-I18N-Collate -f %{oreon_filedir}/perl-I18N-Collate.list
%files -n perl-I18N-Langinfo -f %{oreon_filedir}/perl-I18N-Langinfo.list
%files -n perl-I18N-LangTags -f %{oreon_filedir}/perl-I18N-LangTags.list
%files -n perl-less -f %{oreon_filedir}/perl-less.list
%files -n perl-lib -f %{oreon_filedir}/perl-lib.list
%files -n perl-libnetcfg -f %{oreon_filedir}/perl-libnetcfg.list
%files -n perl-locale -f %{oreon_filedir}/perl-locale.list
%files -n perl-Locale-Maketext-Simple -f %{oreon_filedir}/perl-Locale-Maketext-Simple.list
%files -n perl-Math-Complex -f %{oreon_filedir}/perl-Math-Complex.list
%files -n perl-Memoize -f %{oreon_filedir}/perl-Memoize.list
%files -n perl-meta-notation -f %{oreon_filedir}/perl-meta-notation.list
%files -n perl-Module-Loaded -f %{oreon_filedir}/perl-Module-Loaded.list
%files -n perl-mro -f %{oreon_filedir}/perl-mro.list
%files -n perl-NDBM_File -f %{oreon_filedir}/perl-NDBM_File.list
%files -n perl-Net -f %{oreon_filedir}/perl-Net.list
%files -n perl-NEXT -f %{oreon_filedir}/perl-NEXT.list
%files -n perl-ODBM_File -f %{oreon_filedir}/perl-ODBM_File.list
%files -n perl-Opcode -f %{oreon_filedir}/perl-Opcode.list
%files -n perl-open -f %{oreon_filedir}/perl-open.list
%files -n perl-overload -f %{oreon_filedir}/perl-overload.list
%files -n perl-overloading -f %{oreon_filedir}/perl-overloading.list
%files -n perl-ph -f %{oreon_filedir}/perl-ph.list
%files -n perl-Pod-Functions -f %{oreon_filedir}/perl-Pod-Functions.list
%files -n perl-Pod-Html -f %{oreon_filedir}/perl-Pod-Html.list
%files -n perl-POSIX -f %{oreon_filedir}/perl-POSIX.list
%files -n perl-Safe -f %{oreon_filedir}/perl-Safe.list
%files -n perl-Search-Dict -f %{oreon_filedir}/perl-Search-Dict.list
%files -n perl-SelectSaver -f %{oreon_filedir}/perl-SelectSaver.list
%files -n perl-SelfLoader -f %{oreon_filedir}/perl-SelfLoader.list
%files -n perl-sigtrap -f %{oreon_filedir}/perl-sigtrap.list
%files -n perl-sort -f %{oreon_filedir}/perl-sort.list
%files -n perl-subs -f %{oreon_filedir}/perl-subs.list
%files -n perl-Symbol -f %{oreon_filedir}/perl-Symbol.list
%files -n perl-Sys-Hostname -f %{oreon_filedir}/perl-Sys-Hostname.list
%files -n perl-Term-Complete -f %{oreon_filedir}/perl-Term-Complete.list
%files -n perl-Term-ReadLine -f %{oreon_filedir}/perl-Term-ReadLine.list
%files -n perl-Test -f %{oreon_filedir}/perl-Test.list
%files -n perl-Text-Abbrev -f %{oreon_filedir}/perl-Text-Abbrev.list
%files -n perl-Thread -f %{oreon_filedir}/perl-Thread.list
%files -n perl-Tie -f %{oreon_filedir}/perl-Tie.list
%files -n perl-Tie-File -f %{oreon_filedir}/perl-Tie-File.list
%files -n perl-Tie-Memoize -f %{oreon_filedir}/perl-Tie-Memoize.list
%files -n perl-Time -f %{oreon_filedir}/perl-Time.list
%files -n perl-Time-Piece -f %{oreon_filedir}/perl-Time-Piece.list
%files -n perl-Thread-Semaphore -f %{oreon_filedir}/perl-Thread-Semaphore.list
%files -n perl-Unicode-UCD -f %{oreon_filedir}/perl-Unicode-UCD.list
%files -n perl-User-pwent -f %{oreon_filedir}/perl-User-pwent.list
%files -n perl-vars -f %{oreon_filedir}/perl-vars.list
%files -n perl-vmsish -f %{oreon_filedir}/perl-vmsish.list

%changelog

%autochangelog
