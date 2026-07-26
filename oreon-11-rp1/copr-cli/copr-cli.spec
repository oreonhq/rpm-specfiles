%global source0_hash e1b8a8b4400dcd41a3d607776b100ba79eb8d1c7d0982f13eb310fd580d26427

%global __python %_bindir/python3
%global min_python_copr_version 1.128.1

Name:       copr-cli
Version:    2.4
Release:    3%{?dist}
Summary:    Command line interface for COPR

License:    GPL-2.0-or-later
URL:        https://github.com/fedora-copr/copr

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch:  noarch

Requires:      wget

BuildRequires: asciidoc
BuildRequires: libxslt
BuildRequires: util-linux

Requires:      python3-copr >= %min_python_copr_version
Requires:      python3-jinja2
Requires:      python3-humanize
Requires:      python3-koji

Recommends:    python3-progress
Recommends:    python3-ConfigUpdater
Suggests:      python3-beautifulsoup4

BuildRequires: python3-copr >= %min_python_copr_version
BuildRequires: python3-devel
BuildRequires: python3-jinja2
BuildRequires: python3-humanize
BuildRequires: python3-pytest
BuildRequires: python3-responses
BuildRequires: python3-setuptools
BuildRequires: python3-munch

# We historically shipped empty doc package, uninstall it.
Obsoletes:     copr-cli-doc < 1.72

%description
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latests builds.

This package contains command line interface.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
version="%{version}" %py_build
mv copr_cli/README.rst ./
# convert manages
a2x -d manpage -f manpage man/copr-cli.1.asciidoc

%install
version="%{version}" %py_install
ln -sf %{_bindir}/copr-cli %{buildroot}%{_bindir}/copr
install -d %{buildroot}%{_mandir}/man1
install -p -m 644 man/copr-cli.1 %{buildroot}/%{_mandir}/man1/
install -p man/copr.1 %{buildroot}/%{_mandir}/man1/
install -d %{buildroot}%{_datadir}/cheat
cp -a man/copr-cli.cheat %{buildroot}%{_datadir}/cheat/copr-cli
ln -s %{_datadir}/cheat/copr-cli %{buildroot}%{_datadir}/cheat/copr
install -m 755 copr_cli/package_build_order.py %{buildroot}/%{_bindir}/package-build-order

%check
%{__python3} -m pytest -vv tests

%files
%license LICENSE
%doc README.rst
%{_bindir}/copr
%{_bindir}/copr-cli
%{_mandir}/man1/copr-cli.1*
%{_mandir}/man1/copr.1*
%dir %{_datadir}/cheat
%{_datadir}/cheat/copr-cli
%{_datadir}/cheat/copr
%{python3_sitelib}/*
%{_bindir}/package-build-order

%changelog
%autochangelog
