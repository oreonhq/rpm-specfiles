%global source0_hash db6e5d341d5cf7e49e50aa361243e19087a00ba33742b0855d2685c0b8e721d6

%global _testsdir %{_libexecdir}/%{name}/tests
%global _make_args pkgtestsdir=%%{_testsdir} testsdir=%%{_testsdir}

Name:           kyua
Version:        0.13
Release:        21%{?dist}
Summary:        Testing framework for infrastructure software

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/jmmv/kyua
Source0:        https://github.com/jmmv/kyua/releases/download/kyua-0.13/kyua-0.13.tar.gz
# https://github.com/freebsd/kyua/pull/238
# Fix test failure wrt empty test result on container
Patch0:         kyua-pr238-add-more-info-for-failed-tests.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  libatf-c++-devel >= 0.17
BuildRequires:  libatf-sh-devel >= 0.15
BuildRequires:  pkgconfig(lutok) >= 0.4
BuildRequires:  pkgconfig(sqlite3) >= 3.6.22

Obsoletes:      kyua-cli < 0.10
Provides:       kyua-cli = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      kyua-testers < 0.10
Obsoletes:      kyua-testers-devel < 0.10

%description
Kyua is a testing framework for infrastructure software, originally designed
to equip BSD-based operating systems with a test suite. This means that
Kyua is lightweight and simple, and that Kyua integrates well with various
build systems and continuous integration frameworks.

Kyua features an expressive test suite definition language, a safe runtime
engine for test suites and a powerful report generation engine.

Kyua is for both developers and users, from the developer applying a simple
fix to a library to the system administrator deploying a new release
on a production machine.

Kyua is able to execute test programs written with a plethora of
testing libraries and languages. The library of choice is ATF, for which
Kyua was originally designed, but simple, framework-less test programs and
TAP-compliant test programs can also be executed through Kyua.

%package tests
Summary:        Runtime tests of the Kyua toolchain
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:      kyua-cli-tests < 0.10
Obsoletes:      kyua-testers-tests < 0.10

%description tests
%{summary}.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

# Disable problematic test
# https://github.com/jmmv/kyua/issues/214
sed -e 's/name="stacktrace_test"/&,required_configs="enable_stacktrace"/' -i utils/Kyuafile

%build
%configure \
  --with-doxygen=no   \
  --with-with-atf=yes \
  %{nil}
%make_build %{_make_args}

%install
%make_install %{_make_args} doc_DATA=

%check
# Tests expect dumping core to file which is different from machine to machine
HOME=$(pwd)/check %make_build check %{_make_args}

%files
%license LICENSE
%doc AUTHORS CONTRIBUTORS NEWS.md README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man5/%{name}*.5*

%files tests
%{_libexecdir}/%{name}/

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13-21
- Import
