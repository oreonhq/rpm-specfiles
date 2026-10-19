%global source0_hash c322414975ff6f701149856613afdcd92a7e6939c284c798ae3c85618197efaa
Name:           yara
Version:        4.5.8
Summary:        Pattern matching Swiss knife for malware researchers
URL:            https://VirusTotal.github.io/yara/
VCS:            git:https://github.com/VirusTotal/yara/
License:        BSD-3-Clause
%global         common_description %{expand:
YARA is a tool aimed at (but not limited to) helping malware researchers to
identify and classify malware samples. With YARA you can create descriptions
of malware families (or whatever you want to describe) based on textual or
binary patterns. Each description, a.k.a rule, consists of a set of strings
and a Boolean expression which determine its logic.}
%global         gituser         VirusTotal
%global         gitname         yara
%global         gitdate         20251030
%global         commit          f44a8958e88daa75d765a52a68876f2286d57a51
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%bcond_without  release
%if %{with release}
Release:        1%{?dist}
Source0:        https://github.com/%{gituser}/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
%else
Release:        1%{?dist}
%endif
Patch1:         yara-docs-theme.patch
# oreon:deps
BuildRequires:  /usr/bin/sphinx-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  binutils
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  file
BuildRequires:  file-devel
BuildRequires:  flex
BuildRequires:  gawk
BuildRequires:  gcc
BuildRequires:  git
BuildRequires:  gzip
BuildRequires:  jansson-devel
BuildRequires:  libtool
BuildRequires:  m4
BuildRequires:  openssl-devel
BuildRequires:  protobuf-c-devel
BuildRequires:  protobuf-compiler
BuildRequires:  sed
BuildRequires:  sharutils
BuildRequires:  xz
# /oreon:deps
%description
%{common_description}

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description doc
This package contains documentation for %{name}.
%{common_description}

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.
%{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%if %{with release}
    %autosetup -n %{gitname}-%{version} -p 1 -S git
%else
    %autosetup -n %{gitname}-%{commit} -p 1 -S git
%endif
autoreconf --force --install

%build

%configure --enable-magic --enable-cuckoo --enable-debug --enable-dotnet \
        --enable-macho --enable-dex --enable-pb-tests \
        --with-crypto \
        --htmldir=%{_datadir}/doc/%{name}/html
%make_build
pushd docs
make html
popd
%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la
rm %{buildroot}%{_libdir}/lib%{name}.a
rm -f %{buildroot}%{_datadir}/doc/%{name}/html/.buildinfo
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

export OPENSSL_ENABLE_SHA1_SIGNATURES=yes
make check || (
    echo "===== ./test-suite.log"
    [ -f ./test-suite.log ] && cat ./test-suite.log
    echo "===== /proc/cpu"
    head -n 35 /proc/cpuinfo
    echo "===== /etc/os-release"
    cat /etc/os-release
    echo "===== uname -a"
    uname -a
%ifarch s390x
    true
%else
    false
%endif
)
%files -f %{oreon_filedir}/main.list
%files -n yara-doc -f %{oreon_filedir}/yara-doc.list
%files -n yara-devel -f %{oreon_filedir}/yara-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.5.5-1
- Prepare for Oreon 11 (RP1)
