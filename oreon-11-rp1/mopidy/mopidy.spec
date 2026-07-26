%global source0_hash 5a8e8550ad62a6a59ce42c65b7e8d465da395db19e946916e5f36985d1b2147b

%global homedir %{_sharedstatedir}/%{name}

Name:           mopidy
Version:        4.0.0~a12
Release:        1%{?dist}
Summary:        An extensible music server written in Python

License:        Apache-2.0
URL:            https://mopidy.com/
Source0:        %{pypi_source}
Source1:        mopidy.conf
Patch0:         0001-fix-test-failure-in-mopidy-4.0.0a12.patch

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-tornado
BuildRequires:  python3-Pykka >= 4.0.0
BuildRequires:  python3-requests
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-pytest-mock
BuildRequires:  tox
BuildRequires:  python3-tox-current-env
BuildRequires:  python3-responses
BuildRequires:  python3-gstreamer1
BuildRequires:  gstreamer1-plugins-good
BuildRequires:  libsoup3
BuildRequires:  systemd-rpm-macros
Requires:       python3-gstreamer1
Requires:       libsoup3
Requires:       gstreamer1-plugins-good
Requires:       python3-tornado
Requires:       python3-Pykka >= 4.0.0
Requires:       python3-requests
Suggests:       mopidy-mpd

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

%generate_buildrequires
%pyproject_buildrequires -p

# Create a sysusers.d config file
cat >mopidy.sysusers.conf <<EOF
u mopidy - '%{summary}' %{homedir} -
EOF

%build
%pyproject_wheel

cd docs
PYTHONPATH=../src make SPHINXBUILD=sphinx-build-3 html man
rm _build/html/.buildinfo

%install
%pyproject_install
%pyproject_save_files -l %{name}

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

%check
%tox

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun %{name}.service

%files -f %{pyproject_files}
%license LICENSE
%doc README.rst
# Note: these directories needs to be writable by the mopidy service
%attr(-,%name,%name) %dir %{_var}/cache/%{name}
%attr(-,%name,%name) %dir %{homedir}
                     %dir %{_sysconfdir}/%{name}
                     %dir %{_datadir}/%{name}
                     %dir %{_datadir}/%{name}/conf.d
# Note: users are expected to put streaming service credentials here
%attr(0640,%name,%name) %ghost %config(noreplace) %{_sysconfdir}/%{name}/%{name}.conf
%{_bindir}/%{name}
%{_sbindir}/mopidyctl
%{_unitdir}/%{name}.service
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man8/mopidyctl.8.*
%{_datadir}/%{name}/conf.d/mopidy.conf
%{_sysusersdir}/mopidy.conf

%files doc
%doc docs/_build/html

%changelog
%autochangelog
