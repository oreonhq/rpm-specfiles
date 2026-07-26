%global source0_hash 50d4fb8872b952e57a48e12610e550fa3066eeb57c6c6c75b6a5142418bac19c

Name:           python-lazr-delegates
Version:        2.1.0
Release:        %autorelease
Summary:        Easily write objects that delegate behavior

License:        LGPL-3.0-only
URL:            https://launchpad.net/lazr.delegates
Source:         %{pypi_source lazr.delegates}

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
The lazr.delegates package makes it easy to write objects that delegate behavior
to another object. The new object adds some property or behavior on to the other
object, while still providing the underlying interface, and delegating
behavior.}

%description %_description

%package -n     python3-lazr-delegates
Summary:        %{summary}

%description -n python3-lazr-delegates %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n lazr.delegates-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files lazr

%check
%pyproject_check_import
%tox

%files -n python3-lazr-delegates -f %{pyproject_files}
%{python3_sitelib}/lazr.delegates-%{version}-py%{python3_version}-nspkg.pth

%changelog
%autochangelog
