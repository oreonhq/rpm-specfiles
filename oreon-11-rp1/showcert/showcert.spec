%global source0_hash ae4ccd86b2fc6c5e4701be4c2b08b499966de1312bccbc58496fec69f1e1fcfc
Name:           showcert
Version:        0.4.16
Release:        1%{?dist}
Summary:        inspect TLS certificates presented by remote servers
License:        MIT
URL:            https://github.com/yaroslaff/showcert
Source0:        https://files.pythonhosted.org/packages/source/s/showcert/showcert-%{version}.tar.gz
Patch1:         showcert-remove-dependency-on-python-magic.patch
BuildArch:      noarch
Requires:       (python3dist(magic) or python3dist(file-magic))
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(hatchling) >= 1.27.0
Requires:       python3-showcert = %{version}-%{release}
# /oreon:deps
%description
Simple OpenSSL for humans: all you need for X.509 TLS certificates (and
nothing more).

showcert consist of two CLI utilities: showcert itself - all 'read' operations
with X.509 certificates and gencert - to create certificates for development
purposes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n showcert-%{version}
%py3_shebang_fix showcert/cli/*.py
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main

%check

%pyproject_check_import
export PATH=%{buildroot}%{_bindir}
export PYTHONPATH=%{buildroot}%{python3_sitelib}
showcert --help
gencert --help
%files

%changelog

%autochangelog
