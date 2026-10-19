%global source1_hash 2c805f044d9b9341fa5f18c0f5ab7a05cbb2c9cf52180a01222d937e0779cc06
%global source0_hash 2d0e88d9ffae3a85dafc957a99f64e5f174e4563fd048b9b645ebc3be9e1ace4
%undefine __cmake_in_source_build
%undefine __cmake3_in_source_build
Name:       cscppc
Version:    2.2.7
Release:        1%{?dist}
Summary:        A compiler wrapper that runs Cppcheck in background
License:    GPL-3.0-or-later
URL:        https://github.com/csutils/%{name}
Source0:        https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
Source1:    https://github.com/csutils/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz.asc
Source2:    kdudka.pgp
%ifarch %{ix86} x86_64
%endif
Conflicts: csdiff < 1.8.0
# oreon:deps
BuildRequires:  asciidoc
BuildRequires:  cmake3
BuildRequires:  gcc
BuildRequires:  glibc-static
BuildRequires:  gnupg2
# /oreon:deps
%description
This package contains the cscppc compiler wrapper that runs Cppcheck in
background fully transparently.

%package -n csclng
Summary: A compiler wrapper that runs Clang in background
Requires: clang
Conflicts: csmock-plugin-clang < 1.5.0
%description -n csclng
This package contains the csclng compiler wrapper that runs the Clang analyzer
in background fully transparently.

%package -n csgcca
Summary: A compiler wrapper that runs GCC analyzer in background
Requires: gcc
%description -n csgcca
This package contains the csgcca compiler wrapper that runs GCC analyzer
in background fully transparently.

%package -n csmatch
Summary: A compiler wrapper that runs Smatch in background
%description -n csmatch
This package contains the csmatch compiler wrapper that runs the Smatch analyzer
in background fully transparently.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%cmake3                                       \
    -DPATH_TO_CSCPPC=\"%{_libdir}/cscppc\"    \
    -DPATH_TO_CSCLNG=\"%{_libdir}/csclng\"    \
    -DPATH_TO_CSGCCA=\"%{_libdir}/csgcca\"    \
    -DPATH_TO_CSMATCH=\"%{_libdir}/csmatch\"  \
    -DSTATIC_LINKING=ON
%cmake3_build
%check

%ctest3
%install
%cmake3_install
install -m0755 -d "%{buildroot}%{_libdir}"{,/cs{cppc,clng,gcca,match}}
for i in {,g}cc clang %{_arch}-redhat-linux-gcc
do
    ln -s ../../bin/cscppc  "%{buildroot}%{_libdir}/cscppc/$i"
    ln -s ../../bin/csclng  "%{buildroot}%{_libdir}/csclng/$i"
    ln -s ../../bin/csgcca  "%{buildroot}%{_libdir}/csgcca/$i"
    ln -s ../../bin/csmatch "%{buildroot}%{_libdir}/csmatch/$i"
done
for i in {c,g,clang}++ %{_arch}-redhat-linux-{c,g}++
do
    ln -s ../../bin/cscppc   "%{buildroot}%{_libdir}/cscppc/$i"
    ln -s ../../bin/csclng++ "%{buildroot}%{_libdir}/csclng/$i"
done
%oreon_autofiles csclng usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csgcca usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles csmatch usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n csclng -f %{oreon_filedir}/csclng.list
%files -n csgcca -f %{oreon_filedir}/csgcca.list
%files -n csmatch -f %{oreon_filedir}/csmatch.list

%changelog

%autochangelog
