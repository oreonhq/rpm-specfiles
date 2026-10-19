%global source0_hash 67a99a4655ceec9520ec4bb282845f83cc6c6efd29daf9b3208e5ed50270affb
Name:           khard
Version:        0.21.0
Release:        1%{?dist}
Summary:        An address book for the Linux console
License:        GPL-3.0-only
URL:            https://github.com/scheibler/%{name}
Source0:        https://files.pythonhosted.org/packages/source/k/khard/khard-%{version}.tar.gz
BuildArch:      noarch
Requires:       python3-configobj
Requires:       python3-ruamel-yaml
Requires:       python3-vobject
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 61.0
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.2
Requires:       python3-khard = %{version}-%{release}
# /oreon:deps
%package -n       python3-khard+doc
Summary:        Metapackage for python3-khard doc extras
Requires:       python3-khard = %{version}-%{release}
Provides:       python3dist(khard[doc]) = %{version}-%{release}

%description -n python3-khard+doc
Metapackage for python3-khard doc extras.

%package -n       python3-khard+typing
Summary:        Metapackage for python3-khard typing extras
Requires:       python3-khard = %{version}-%{release}
Provides:       python3dist(khard[typing]) = %{version}-%{release}

%description -n python3-khard+typing
Metapackage for python3-khard typing extras.

%description
Khard is an address book for the Linux console. It creates, reads, modifies and
removes carddav address book entries at your local machine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}%{_datadir}/khard/examples/
mkdir -p %{buildroot}%{_datadir}/khard/examples/davcontroller/
install -p -m 0644 misc/davcontroller/davcontroller.py %{buildroot}%{_datadir}/khard/examples/davcontroller/davcontroller.py
mkdir -p %{buildroot}%{_datadir}/khard/examples/sdiff/
install -p -m 0644 misc/sdiff/sdiff_khard_wrapper.sh %{buildroot}%{_datadir}/khard/examples/sdiff/sdiff_khard_wrapper.sh
install -p -d misc/twinkle %{buildroot}%{_datadir}/khard/examples/twinkle
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -p -m 0644 misc/zsh/_email-khard %{buildroot}%{_datadir}/zsh/site-functions/_khard
install -p -m 0644 misc/zsh/_khard %{buildroot}%{_datadir}/zsh/site-functions/_khard
%oreon_autofiles main

%check

%pyproject_check_import
%files

%changelog

%autochangelog
