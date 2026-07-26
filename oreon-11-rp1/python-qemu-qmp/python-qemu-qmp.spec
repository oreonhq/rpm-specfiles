%global source0_hash 1d1b9a9a5d57edfe2de3a1d888612823b09aff946951a902e79e9655a2aabbfd

Name:           python-qemu-qmp
Version:        0.0.5
Release:        2%{?dist}
Summary:        QEMU Monitor Protocol library

License:        GPL-2.0-only AND LGPL-2.0-or-later
# NB:           qemu/qmp/legacy.py is GPLv2 only.
#               Everything else installed is LGPLv2+.
URL:            https://pypi.org/project/qemu.qmp
Source0:        %{pypi_source qemu_qmp}

BuildArch:      noarch
BuildRequires:  gnupg2
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%global _description %{expand:
qemu.qmp is a QEMU Monitor Protocol (“QMP”) library written in Python,
using asyncio. It is used to send QMP messages to running QEMU
emulators. It requires Python 3.8+ and has no mandatory
dependencies. This library can be used to communicate with QEMU
emulators, the QEMU Guest Agent (QGA), the QEMU Storage Daemon (QSD), or
any other utility or application that speaks QMP.}

%description %_description

%package -n     python3-qemu-qmp
Summary:        %{summary}

%description -n python3-qemu-qmp %_description

%package        doc
Summary:        Documentation for the %{summary}

%description    doc %_description

This package provides offline HTML documentation for python3-qemu-qmp.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n qemu_qmp-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
PYTHONPATH=${PWD} sphinx-build-3 docs html
PYTHONPATH=${PWD} sphinx-build-3 -b man docs man
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%pyproject_install
# Explicitly exclude the 'qmp-tui' script shim from rpm release.
#
# It is meant to be included with the 'tui' extras, which are not being
# packaged here at this time. Without the extras, this shim merely
# prints an error and exits.
rm %{buildroot}%{_bindir}/qmp-tui

install -Dpm 0644 man/*.1 -t %{buildroot}%{_mandir}/man1/

# Use PEP420 namespace name instead of package name:
# https://bugzilla.redhat.com/show_bug.cgi?id=1935266
%pyproject_save_files qemu

%check
%pyproject_check_import -e qemu.qmp.qmp_tui
%pytest -v

%files -n python3-qemu-qmp -f %{pyproject_files}
%license LICENSE LICENSE_GPL2
%doc README.rst
%{_bindir}/qmp-shell
%{_bindir}/qmp-shell-wrap
%{_mandir}/man1/qmp-shell.1*
%{_mandir}/man1/qmp-shell-wrap.1*

%files doc
%license LICENSE LICENSE_GPL2
%doc html

%changelog
%autochangelog
