%global source0_hash 5634d2c22a18a84b421f1a9c3ea1a05c17819caeb3701938fec6b8dea3db8e8b
%if ! 0%{?rel_build:1}
    %global rel_build 1
%endif
%if 0%{?rel_build}
    %global gittar              aexpect-%{version}.tar.gz
%else
    %if ! 0%{?commit:1}
        %global commit          a542688c95dd3d5a55def634f998e9ac635d8304
    %endif
    %if ! 0%{?commit_date:1}
        %global commit_date     20210602
    %endif
    %global shortcommit         %(c=%{commit};echo ${c:0:8})
    %global gitrel              .%{commit_date}git%{shortcommit}
    %global gittar              aexpect-%{shortcommit}.tar.gz
%endif
%global with_tests 0
Name: python-aexpect
Version: 1.8.0
Release:        1%{?dist}
Summary:        A python library to control interactive applications
License: GPL-2.0-or-later
URL: https://github.com/avocado-framework/aexpect
%if 0%{?rel_build}
Source0:        https://github.com/avocado-framework/aexpect/archive/%{version}/aexpect-%{version}.tar.gz
%else
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Aexpect is a python library used to control interactive applications, very
similar to pexpect. You can use it to control applications such as ssh, scp
sftp, telnet, among others.

%package -n python%{python3_pkgversion}-aexpect
Summary:        A python library to control interactive applications
%description -n python%{python3_pkgversion}-aexpect
Aexpect is a python library used to control interactive applications, very
similar to pexpect. You can use it to control applications such as ssh, scp
sftp, telnet, among others.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if 0%{?rel_build}
%autosetup -n aexpect-%{version} -p 1
%else
%autosetup -n aexpect-%{commit} -p 1
%endif

%build

%py3_build
%install
%py3_install
ln -s aexpect_helper %{buildroot}%{_bindir}/aexpect_helper-%{python3_pkgversion}
ln -s aexpect_helper %{buildroot}%{_bindir}/aexpect_helper-%{python3_version}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-aexpect -f %{oreon_filedir}/python3-aexpect.list

%changelog

%autochangelog
