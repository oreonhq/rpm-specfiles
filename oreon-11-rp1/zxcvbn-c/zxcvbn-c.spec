%global source0_hash 11e39f6776f9c82c68b2acb94336e32697d4ab6cdb4ac16f9583ccbdd735113a
%global forgeurl https://github.com/tsyrogit/zxcvbn-c
Version:        2.6
%forgemeta
Name:           zxcvbn-c
Release:        1%{?dist}
Summary:        C/C++ version of the zxcvbn password strength estimator
License:        MIT
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  gcc-c++
# /oreon:deps
%description
This is a C/C++ implementation of the zxcvbn password strength estimation.
The code is intended to be included as part of the source of a C/C++ program.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup

%build

%make_build
%install
%{__mkdir_p} %{buildroot}%{_libdir}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__mkdir_p} %{buildroot}{%{_includedir},%{_datadir}}/zxcvbn
install -p -m 0644 *.h %{buildroot}%{_includedir}/zxcvbn
cp -a libzxcvbn.so* %{buildroot}%{_libdir}
install -p -m 0755 dictgen %{buildroot}%{_bindir}
install -p -m 0644 zxcvbn.dict %{buildroot}%{_datadir}/zxcvbn
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

make test
%files -f %{oreon_filedir}/main.list
%files -n zxcvbn-c-devel -f %{oreon_filedir}/zxcvbn-c-devel.list

%changelog

%autochangelog
