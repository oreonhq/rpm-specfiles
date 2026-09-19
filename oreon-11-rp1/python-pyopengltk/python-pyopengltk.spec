%global source0_hash 4ec9bd44e5b3a8a4f3901d611b572c6d55463450ecf7d20bc51c00771b669650

%global pypi_name pyopengltk

Name:           python-%{pypi_name}
Version:        0.0.4
Release:        %{autorelease}
Summary:        An OpenGL frame for pyopengl-tkinter based on ctype

License:        MIT
URL:            https://github.com/jonwright/pyopengltk
Source:         %{pypi_source %{pypi_name}}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-tkinter
BuildRequires:  libX11

%global _description %{expand:
Tkinter - OpenGL Frame using ctypes

An opengl frame for pyopengl-tkinter based on ctypes (no togl
compilation).

Collected together by Jon Wright, Jan 2018.}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       python3-tkinter
Requires:       libX11

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}

# Remove MacOS and Windows modules
rm -vf pyopengltk/darwin.py pyopengltk/win32.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
# Upstream doesn't provide tests
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
