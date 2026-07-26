%global source0_hash 6576082eed88a065d22d958eaf6b6e9973a597d99e887f9f0140f331ac2f65f2

%global pypi_name xword_dl

Name:           python-xword-dl
Version:        2025.10.14
Release:        %autorelease
Summary:        Download tool for online crossword puzzles

License:        MIT
URL:            https://github.com/thisisparker/xword-dl
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  sed

%global _description %{expand:
xword-dl is a command-line tool to download .puz files for online crossword
puzzles from supported outlets or arbitrary URLs with embedded crossword
solvers. For a supported outlet, you can easily download the latest puzzle, or
specify one from the archives.}

%description %_description

%package -n     python3-xword-dl
Summary:        %{summary}

%description -n python3-xword-dl %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Relax dependencies version pinning
rm uv.lock
sed -i pyproject.toml -e 's/==/>=/g'

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-xword-dl -f %{pyproject_files}
%doc README.md
%{_bindir}/xword-dl

%changelog
%autochangelog
