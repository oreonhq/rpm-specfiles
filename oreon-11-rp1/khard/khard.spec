%global source0_hash 178f32ccf01c050b5cd9e736282583de9a6445fd98e00388df792207629bbdd0

Name:           khard
Version:        0.20.0
Release:        5%{?dist}
Summary:        An address book for the Linux console

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://github.com/scheibler/%{name}
Source0:        %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools_scm
Requires:       python3-configobj
Requires:       python3-ruamel-yaml
Requires:       python3-vobject

%description
Khard is an address book for the Linux console. It creates, reads, modifies and
removes carddav address book entries at your local machine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l '*'
mkdir -p %{buildroot}%{_datadir}/khard/examples/
mkdir -p %{buildroot}%{_datadir}/khard/examples/davcontroller/
install -p -m 0644 misc/davcontroller/davcontroller.py %{buildroot}%{_datadir}/khard/examples/davcontroller/davcontroller.py
mkdir -p %{buildroot}%{_datadir}/khard/examples/sdiff/
install -p -m 0644 misc/sdiff/sdiff_khard_wrapper.sh %{buildroot}%{_datadir}/khard/examples/sdiff/sdiff_khard_wrapper.sh
install -p -d misc/twinkle %{buildroot}%{_datadir}/khard/examples/twinkle
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions/
install -p -m 0644 misc/zsh/_email-khard %{buildroot}%{_datadir}/zsh/site-functions/_khard
install -p -m 0644 misc/zsh/_khard %{buildroot}%{_datadir}/zsh/site-functions/_khard

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc CHANGES README.md todo.txt
%{_bindir}/khard
%{_datadir}/khard/
%{_datadir}/zsh/site-functions/

%changelog
%autochangelog
