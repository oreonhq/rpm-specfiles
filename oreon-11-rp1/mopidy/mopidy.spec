%global source0_hash cdceb64e1574d708396bf8ee9f71460df3614dbb9c6aee36b24e23b90492501f
%global homedir %{_sharedstatedir}/%{name}
Name:           mopidy
Version:        4.0.4
Release:        1%{?dist}
Summary:        An extensible music server written in Python
License:        Apache-2.0
URL:            https://mopidy.com/
Source0:        https://files.pythonhosted.org/packages/source/m/mopidy/mopidy-%{version}.tar.gz
Source1:        mopidy.conf
Patch0:         0001-fix-test-failure-in-mopidy-4.0.0a12.patch
BuildArch:      noarch
Requires:       python3-gstreamer1
Requires:       libsoup3
Requires:       gstreamer1-plugins-good
Requires:       python3-tornado
Requires:       python3-Pykka >= 4.0.0
Requires:       python3-requests
Suggests:       mopidy-mpd
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 78
BuildRequires:  python3dist(setuptools-scm) >= 8.2
Requires:       python3-mopidy = %{version}-%{release}
# /oreon:deps
%description
Mopidy plays music from local disk, and a plethora of streaming services and
sources. You edit the playlist from any phone, tablet, or computer using a
variety of MPD and web clients.

%package doc
BuildRequires:  python3-graphviz
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinx-autodoc-typehints
Summary:        Documentation for Mopidy
BuildArch:      noarch
%description doc
Documentation for Mopidy, an extensible music server written in Python.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-4.0.0a12 -p1
#HACK! revert to %%autosetup -n %%{name}-%%{version} -p1
rm -f setup.cfg # HACK: work around https://github.com/tox-dev/tox/issues/3602

%build

%pyproject_wheel
cd docs
PYTHONPATH=../src make SPHINXBUILD=sphinx-build-3 html man
rm _build/html/.buildinfo
%install
%pyproject_install
install -d -m 0755 %{buildroot}%{homedir}
install -d -m 0755 %{buildroot}%{_var}/cache/%{name}
install -d -m 0755 %{buildroot}%{_sysconfdir}/%{name}
touch %{buildroot}%{_sysconfdir}/%{name}/%{name}.conf
install -p -D extra/mopidyctl/mopidyctl %{buildroot}%{_sbindir}/mopidyctl
install -p -D -m 0644 docs/_build/man/mopidy.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -p -D -m 0644 extra/mopidyctl/mopidyctl.8 %{buildroot}%{_mandir}/man8/mopidyctl.8
install -p -D -m 0644 extra/systemd/mopidy.service %{buildroot}%{_unitdir}/%{name}.service
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/%{name}/conf.d/mopidy.conf
install -m0644 -D mopidy.sysusers.conf %{buildroot}%{_sysusersdir}/mopidy.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%tox
%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun %{name}.service
%files
%files -n mopidy-doc -f %{oreon_filedir}/mopidy-doc.list

%changelog

%autochangelog
