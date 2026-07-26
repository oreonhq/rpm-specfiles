%global source0_hash df47147b87f6ec952948ce030e1b20f39c1f7adc10285c3f3196adb582c0e8b0

# Conditional for release vs. snapshot builds. Set to 1 for release build.
%if ! 0%{?rel_build:1}
    %global rel_build 1
%endif

# Settings used for build from snapshots.
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

# Selftests are provided but skipped because they use unsupported tooling.
%global with_tests 0

Name: python-aexpect
Version: 1.6.2
Release: 19%{?gitrel}%{?dist}
Summary: A python library to control interactive applications

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: https://github.com/avocado-framework/aexpect

%if 0%{?rel_build}
Source0: %{url}/archive/%{version}/%{gittar}
%else
Source0: %{url}/archive/%{commit}/%{gittar}
%endif

BuildArch: noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Aexpect is a python library used to control interactive applications, very
similar to pexpect. You can use it to control applications such as ssh, scp
sftp, telnet, among others.

%package -n python%{python3_pkgversion}-aexpect
Summary: %{summary}

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

%if %{with_tests}
%check
selftests/checkall
%endif

%files -n python%{python3_pkgversion}-aexpect
%license LICENSE
%doc README.rst
%{python3_sitelib}/aexpect/
%{python3_sitelib}/aexpect-%{version}-py%{python3_version}.egg-info/
%{_bindir}/aexpect_helper*

%changelog
%autochangelog
