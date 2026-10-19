%global source0_hash ebe473e17b13f1d1f16d0009689576625796947a711e14aec29530f39560c7c2
Name:           easyloggingpp
Version:        9.97.1
Release:        1%{?dist}
Epoch:          1
Summary:        C++ logging library
License:        MIT
URL:            https://github.com/abumq/easyloggingpp
Source0:        https://github.com/abumq/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:          %{url}/pull/817.patch
Patch:          %{url}/pull/818.patch
Patch:          %{url}/pull/863.patch
%global debug_package %{nil}
%global common_description %{expand:
Easylogging++ is an efficient logging library for C++ applications. It is
extremely powerful, highly extendable and configurable to a user’s
requirements. It provides the ability to write your own sinks (via featured
referred as LogDispatchCallback). This library is currently used by hundreds of
open-source projects on github and other open-source source control management
sites.}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(gtest)
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  hardlink
BuildRequires:  ninja-build
BuildRequires:  symlinks
# /oreon:deps
%description %{common_description}

%package        devel
Summary:        Development files for Easylogging++
BuildArch:      noarch
Provides:       easyloggingpp-static = %{?epoch:%{epoch}:}%{version}-%{release}
%description    devel %{common_description}

The easyloggingpp-devel package contains libraries and header files for
developing applications that use Easylogging++.

%package        doc
Summary:        Documentation and examples for Easylogging++
BuildArch:      noarch
Requires:       easyloggingpp-devel = %{?epoch:%{epoch}:}%{version}-%{release}
%description    doc %{common_description}

The easyloggingpp-doc package contains documentation and examples for
developing applications that use Easylogging++.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n easyloggingpp-%{version} -p1
# Remove .gitignore and similar files that might accidentally be packaged,
# especially in the samples.
find . -type f \( -name '.git*' -o -name '.travis*' \) -print -delete
find . -depth -type d -name '.vs' -print -execdir rm -rvf '{}' ';'
# Fix CRNL line endings
dos2unix --keepdate samples/Qt/fast-dictionary/words.txt
find samples/VC++ -type f -execdir dos2unix --keepdate '{}' '+'

%conf
%cmake -GNinja -Dtest:BOOL=TRUE

%build

%cmake_build
%install
%cmake_install
install -d '%{buildroot}%{_pkgdocdir}'
cp -rvp *.md doc samples '%{buildroot}%{_pkgdocdir}'
find '%{buildroot}%{_pkgdocdir}/samples' -type f \
    \( -name 'easylogging++.cc' -o -name 'easylogging++.h' \) |
  while read -r fn
  do
    ln -svf "%{buildroot}%{_includedir}/$(basename "${fn}")" "${fn}"
    symlinks -c -o "${fn}"
  done
hardlink '%{buildroot}%{_pkgdocdir}/samples'
(
  find samples/ -type d -printf '\045doc \045dir \045{_pkgdocdir}/%p\n'
  find samples/ -type f -name 'LICENCE' \
      -printf '\045license \045{_pkgdocdir}/%p\n'
  find samples/ -type f ! -name 'LICENCE' \
      -printf '\045doc \045{_pkgdocdir}/%p\n'
) | tee samples.files
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{_vpath_builddir}/easyloggingpp-unit-tests \
    --gtest_filter=-CommandLineArgsTest.LoggingFlagsArg
%files -f %{oreon_filedir}/main.list
%files -n easyloggingpp-devel -f %{oreon_filedir}/easyloggingpp-devel.list
%files -n easyloggingpp-doc -f %{oreon_filedir}/easyloggingpp-doc.list

%changelog

%autochangelog
