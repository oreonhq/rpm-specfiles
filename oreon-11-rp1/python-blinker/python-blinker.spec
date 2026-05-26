# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 9b02df578ec0aadd5e800e5f09281e80abddab5e0f74b4b88694f06c9956b6aa
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global mod_name blinker

Name:           python-blinker
Version:        1.9.0
Release:        8%{?dist}
Summary:        Fast, simple object-to-object and broadcast signaling

License:        MIT
URL:            https://github.com/pallets-eco/blinker
Source0:        https://github.com/pallets-eco/blinker/archive/1.9.0/blinker-1.9.0.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description\
Blinker provides a fast dispatching system that allows any number\
of interested parties to subscribe to events, or "signals".

%description %_description

%package -n python3-blinker
Summary:        Fast, simple object-to-object and broadcast signaling
%{?python_provide:%python_provide python3-blinker}

%description -n python3-blinker
Blinker provides a fast dispatching system that allows any number
of interested parties to subscribe to events, or "signals".

%prep
%oreon_verify_sources
%autosetup -n %{mod_name}-%{version}
# requirements in tests.txt are way too tight
mv requirements/tests.in requirements/tests.txt

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{mod_name}

%check
# Ignore DeprecationWarnings for now: they come from Python 3.14
# and leak through python-pytest-asyncio to other packages
%tox -- -- -W ignore::DeprecationWarning

%files -n python3-blinker -f %{pyproject_files}
%doc CHANGES.rst LICENSE.txt README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9.0-8
- Prepare for Oreon 11 (RP1)
