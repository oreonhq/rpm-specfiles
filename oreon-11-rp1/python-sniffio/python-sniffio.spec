%global source0_hash f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc

Name:           python-sniffio
Version:        1.3.1
Release:        %autorelease
Summary:        Sniff out which async library your code is running under
License:        MIT OR Apache-2.0
URL:            https://github.com/python-trio/sniffio
Source:         %{pypi_source sniffio}
BuildArch:      noarch

%global common_description %{expand:
You're writing a library.  You've decided to be ambitious, and support multiple
async I/O packages, like Trio, and asyncio, and ... You've written a bunch of
clever code to handle all the differences.  But... how do you know which piece
of clever code to run?  This is a tiny package whose only purpose is to let you
detect which async library your code is running under.}

%description %{common_description}

%package -n python3-sniffio
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  %{py3_dist pytest}

%description -n python3-sniffio %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sniffio-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sniffio

%check
%pytest --verbose

%files -n python3-sniffio -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
