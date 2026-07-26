%global source0_hash 48b01ee6e6c818472150da0709cb7a0968ac0636b758d11fa44e3cbfd093ccf4

Name:           python-pygments-better-html
Version:        0.1.5
Release:        9%{?dist}
Summary:        Better line numbers for Pygments HTML

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/Kwpolska/pygments_better_html
Source0:        %{pypi_source pygments_better_html}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
This library provides improved line numbers for the Pygments HTML formatter.
}

%description %_description

%package -n python3-pygments-better-html
Summary: %{summary}

%description -n python3-pygments-better-html %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pygments_better_html-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pygments_better_html

%check
%pyproject_check_import

%files -n python3-pygments-better-html -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
%autochangelog
