%global source0_hash 6fd5e0eaa40ff349959d1cee2872eee90ae32065cc5df9714b1066981535acde

Name:           python-pyclip
Version:        0.7.0
Release:        15%{?dist}
Summary:        Cross-platform Clipboard module for Python with binary support

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/spyoungtech/pyclip
Source:         %{url}/archive/v%{version}/pyclip-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description \
Cross-platform Clipboard module for Python with binary support

%description %{_description}

%package -n     python3-pyclip
Summary:        %{summary}

%description -n python3-pyclip %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pyclip-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyclip

%files -n python3-pyclip -f %{pyproject_files}
%license LICENSE
%doc docs/README.md
%{_bindir}/pyclip

%changelog
%autochangelog
