%global source0_hash 7a0b6ae4628dd0c31a5ceb51258918d9bbdd3ad851388837225826b228ee504f

Name:           python-trezor
Version:        0.13.10
Release:        8%{?dist}
Summary:        Python library and command-line client for communicating with Trezor Hardware Wallet

License:        LGPL-3.0-only
URL:            https://github.com/trezor/trezor-firmware/tree/main/python
Source0:        %{pypi_source trezor}

# Remove click's upper version bound
Patch:          remove_click_upper_bound.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pkgconfig(bash-completion)

#Unit tests
BuildRequires:  python3-pytest
BuildRequires:  python3-typing-extensions
BuildRequires:  python3-requests
BuildRequires:  %{py3_dist construct-classes}
#check_import
BuildRequires:  python3-qt5

%description
%{summary}.

%package -n python3-trezor
Summary:        %{summary}
Requires:       %{py3_dist hidapi}
Requires:       trezor-common >= 2.3.6

%description -n python3-trezor
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n trezor-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l trezorlib

install -Dpm 644 bash_completion.d/trezorctl.sh %{buildroot}%{bash_completions_dir}/trezorctl

%check
%pyproject_check_import

#Missing dependency on stellar_sdk
%{pytest} \
  tests/test_btc.py \
  tests/test_cosi.py \
  tests/test_protobuf_encoding.py \
  tests/test_protobuf_misc.py \
  tests/test_tools.py \
  tests/test_transport.py

%files -n python3-trezor -f %{pyproject_files}
%doc AUTHORS
%doc CHANGELOG.md
%doc README.md
%{_bindir}/trezorctl
%{bash_completions_dir}/trezorctl

%changelog
%autochangelog
