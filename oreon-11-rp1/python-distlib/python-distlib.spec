%global source0_hash f152097224a0ae24be5a0f6bae1b9359af82133bce63f98a95f86cae1aede9ed

Name:           python-distlib
Version:        0.4.3
Release:        %autorelease
Summary:        Low-level components of distutils2 and higher-level APIs

License:        Python-2.0.1
URL:            https://github.com/pypa/distlib
Source:         https://files.pythonhosted.org/packages/c9/02/bd72be9134d25ed783ecbbc38a539ffaefbf90c78418c7fb7229600dbac7/distlib-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%description
Distlib contains low-level components of distutils2 and higher-level APIs.


%package -n python3-distlib
Summary:        %{summary}

%description -n python3-distlib
Distlib contains low-level components of distutils2 and higher-level APIs.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n distlib-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files distlib


%check
%pyproject_check_import


%files -n python3-distlib -f %{pyproject_files}
%doc README.rst
%license LICENSE.txt


%changelog
%autochangelog
