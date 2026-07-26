%global source0_hash 5dd01cf61975a8a57213cdef5ed870e936032f13fe93d60ddf659ffb9cf73c6a

Name:           python-cmarkgfm
Version:        2024.11.20
Release:        %autorelease
Summary:        Minimal bindings to GitHub's fork of cmark

License:        MIT
URL:            https://github.com/theacodes/cmarkgfm
Source:         %{pypi_source cmarkgfm}

BuildRequires:  gcc

%description
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%package -n     python3-cmarkgfm
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%description -n python3-cmarkgfm
Bindings to GitHub's cmark Minimalist bindings to GitHub's fork of cmark.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cmarkgfm-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l cmarkgfm

%check
%pytest -v tests

%files -n python3-cmarkgfm -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
