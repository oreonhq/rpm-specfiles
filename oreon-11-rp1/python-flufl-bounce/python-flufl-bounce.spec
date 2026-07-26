%global source0_hash 25504aeb976ec0fe5a19cd6c413a3410cb514fdcdbdca9f9b5d8d343a8603831

Name:           python-flufl-bounce
Version:        4.0
Release:        %autorelease
Summary:        Email bounce detectors

License:        Apache-2.0
URL:            https://fluflbounce.readthedocs.io/en/latest/
Source:         %{pypi_source flufl.bounce}

BuildArch:      noarch
BuildRequires:  python3-devel

# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
The flufl.bounce library provides a set of heuristics and an API for detecting
the original bouncing email addresses from a bounce message. Many formats found
in the wild are supported, as are VERP and RFC 3464 (DSN).}

%description %_description

%package -n     python3-flufl-bounce
Summary:        %{summary}

%description -n python3-flufl-bounce %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n flufl.bounce-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files flufl

%check
%pyproject_check_import

%files -n python3-flufl-bounce -f %{pyproject_files}
%{python3_sitelib}/flufl.bounce-%{version}-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
