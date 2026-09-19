%global source0_hash dd72c7cb496f5e31abe5ffd24d166902afb866d92589850a5da1f0139ba9971e

%global forgeurl https://github.com/SpamExperts/pyzor
%global commit   2be00c3f802d541f6b86afb4fc3a84a9820eddb5

Name:           pyzor
Version:        1.0.0
Release:        46%{?dist}
Summary:        Collaborative spam filtering system
License:        GPL-2.0-only
%forgemeta
URL:            %forgeurl
Source0:        %forgesource
Patch0:         https://github.com/SpamExperts/pyzor/pull/168.patch#/pyzor-1.0.0-python-3.13.patch

BuildArch:      noarch
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-pytest
BuildRequires:  python%{python3_pkgversion}-setuptools
# No python3-redis (yet?) in EPEL, only in Fedora
%if 0%{?fedora}  
BuildRequires:  python%{python3_pkgversion}-redis
%endif

%description
Pyzor is a collaborative, networked system to detect
and block spam using identifying digests of messages.
Pyzor is similar to Vipul's Razor except implemented
in python, and using fully open source servers.

Pyzor can be used either standalone, or to augment the
spam filtering ability of spamassassin.  spamassassin
is highly recommended.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%py3_build

%install
%py3_install
install -d -m 755 %{buildroot}%{_sysconfdir}/%{name}

# Tests are failing without python3-redis, even it's optional
%if 0%{?fedora}
%check
%pytest tests/unit/
%endif

%files
%license COPYING
%doc config/ README.rst THANKS
%dir %{_sysconfdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/%{name}-migrate
%{_bindir}/%{name}d
%{python3_sitelib}/%{name}*

%changelog
%autochangelog
