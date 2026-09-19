%global source0_hash 0952cd77b9d0869d4c7cf2adef76130459541425c1f1b2bef0e287e51a27e71e

# Explicitly define on RHEL8 to avoid an unnecessary dependency on python36
%if %{defined el8}
%global __python3 %{_libexecdir}/platform-python
%endif

Name:           centpkg
Version:        0.10.3
Release:        1%{?dist}
Summary:        CentOS utility for working with dist-git
License:        GPL-2.0-or-later
URL:            https://gitlab.com/CentOS/common/centpkg
Source0:        %{url}/-/archive/%{version}/centpkg-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
# runtime requirements for test suite
BuildRequires:  python3-cryptography
BuildRequires:  python3-GitPython
BuildRequires:  python3-gitlab
BuildRequires:  python3-pycurl
BuildRequires:  python3-rpkg >= 1.6.5

# /etc/koji.conf.d/stream.conf was previously part of streamkoji
Conflicts:      streamkoji < 1.1-3

%description
Provides the centpkg command for working with dist-git.

%package sig
Summary:        CentOS SIG utility for working with dist-git
Requires:       %{name} = %{version}-%{release}

%description sig
Provides the centpkg-sig command for working with dist-git.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%{python3} doc/centpkg_man_page.py > centpkg.1

%install
%pyproject_install
%pyproject_save_files -l %{name}
install -D -p -m 0644 src/stream.conf      %{buildroot}%{_sysconfdir}/koji.conf.d/stream.conf
install -D -p -m 0644 src/centpkg.conf     %{buildroot}%{_sysconfdir}/rpkg/centpkg.conf
install -D -p -m 0644 src/centpkg-sig.conf %{buildroot}%{_sysconfdir}/rpkg/centpkg-sig.conf
install -D -p -m 0644 src/centpkg.bash     %{buildroot}%{_datadir}/bash-completion/completions/centpkg
install -D -p -m 0644 centpkg.1            %{buildroot}%{_mandir}/man1/centpkg.1

%check
%pyproject_check_import

PYTHONPATH=%{buildroot}%{python3_sitelib} %{python3} -m unittest discover --verbose

%files -f %{pyproject_files}
%doc README.md
%config(noreplace) %{_sysconfdir}/koji.conf.d/stream.conf
%config(noreplace) %{_sysconfdir}/rpkg/centpkg.conf
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/centpkg
%{_mandir}/man1/centpkg.1*

%files sig
%{_bindir}/%{name}-sig
%config(noreplace) %{_sysconfdir}/rpkg/centpkg-sig.conf

%changelog
%autochangelog
