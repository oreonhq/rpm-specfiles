%global source0_hash 98c2ea2ce3e57ae836b1dc6bea0af017a7cb4c6692366fd3baecf1a2220f233c

%global pypi_name glfw

Name:           python-%{pypi_name}
Version:        2.7.0
Release:        %{autorelease}
Summary:        A ctypes-based wrapper for GLFW3

%global forgeurl https://github.com/FlorianRhiem/pyGLFW
%forgemeta

License:        MIT
URL:            %forgeurl
Source:         %forgesource

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  glfw

%global _description %{expand:
This module provides Python bindings for GLFW (on GitHub: glfw/glfw).
It is a ctypes wrapper which keeps very close to the original GLFW API,
except for:

- function names use the pythonic `words_with_underscores` notation
  instead of `camelCase`
- `GLFW_` and `glfw` prefixes have been removed, as their function is
  replaced by the module namespace (you can use `from glfw.GLFW import *`
  if you prefer the naming convention used by the GLFW C API)
- structs have been replaced with Python sequences and namedtuples
- functions like `glfwGetMonitors` return a list instead of a pointer
  and an object count
- Gamma ramps use floats between 0.0 and 1.0 instead of unsigned shorts
  (use `glfw.NORMALIZE_GAMMA_RAMPS=False` to disable this)
- GLFW errors are reported as glfw.GLFWError warnings if no error
  callback is set (use `glfw.ERROR_REPORTING=False` to disable this,
  set it to `warn` instead to issue warnings, set it to `log` to log it
  using the `glfw` logger or set it to a dict to define the behavior
  for specific error codes)
- instead of a sequence for `GLFWimage` structs, PIL/pillow `Image`
  objects can be used}

%description %_description

%package -n python3-%{pypi_name}
Summary:        %{summary}
Requires:       glfw

%description -n python3-%{pypi_name} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
# Upstream does not provide tests
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst CHANGELOG.md

%changelog
%autochangelog
