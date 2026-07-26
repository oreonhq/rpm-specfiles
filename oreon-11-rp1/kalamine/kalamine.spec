%global source0_hash 1ffadf9b59ea17587bf7a6e7213b8f8b462d9bf27d5f5fdc81cf4a6323d94036

Name:           kalamine
Version:        0.38
Release:        %autorelease
Summary:        Cross-platform Keyboard Layout Maker
License:        MIT
URL:            https://github.com/OneDeadKey/kalamine
Source:         %{pypi_source kalamine}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-lxml

%description
A text-based, cross-platform Keyboard Layout Maker.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# rpmlint: E: zero-length
mv kalamine/generators/{__init.py__,__init__.py}
# rpmlint: E: non-executable-script
sed -e '1{/^#!/d}' -i kalamine/{__init__.py,cli*.py}
# remove Windows-only CLI
sed -e '/wkalamine/d' -i pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l kalamine

%check
%{py3_test_envvars} %{python3} -m kalamine.cli build layouts/*.toml
%{py3_test_envvars} %{python3} -m kalamine.cli new test.toml
%pytest

%files -f %{pyproject_files}
%doc docs/*.md
%{_bindir}/kalamine
%{_bindir}/xkalamine

%changelog
%autochangelog
