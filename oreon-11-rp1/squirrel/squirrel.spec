%global source0_hash 02805414cfadd5bbb921891d3599b83375a40650abd6404a8ab407dc5e86a996

Name:           squirrel
Version:        3.2
Release:        6%{?dist}
Summary:        High level imperative/OO programming language

License:        Zlib
URL:            http://squirrel-lang.org/
Source0:        https://github.com/albertodemichelis/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# borrowed from Debian with s/squirrel/sq/g
Source1:        sq.1
# backported fixes and Fedora specific changes
# https://github.com/sharkcz/squirrel/tree/fedora
Patch0:         squirrel-3.2-fedora.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

%description
Squirrel is a high level imperative/OO programming language, designed
to be a powerful scripting tool that fits in the size, memory bandwidth,
and real-time requirements of applications like games.

%package libs
Summary:        Libraries needed to run Squirrel scripts

%description libs
Libraries needed to run Squirrel scripts.

%package devel
Summary:        Development files needed to use Squirrel libraries
Requires:       %{name}-libs = %{version}-%{release}

%description devel
Development files needed to use Squirrel libraries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake -DDISABLE_STATIC=1
%cmake_build

pushd doc
make html
popd

%install
%cmake_install

mkdir -p %{buildroot}%{_mandir}/man1/
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/

%files
%license COPYRIGHT
%{_bindir}/sq
%{_mandir}/man1/sq.1*

%files libs
%license COPYRIGHT
%doc README HISTORY
%{_libdir}/libsqstdlib.so.%{version}
%{_libdir}/libsquirrel.so.%{version}

%files devel
%doc doc/build/html
%{_includedir}/%{name}
%{_libdir}/cmake/%{name}
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/libsqstdlib.so
%{_libdir}/libsquirrel.so

%changelog
%autochangelog
