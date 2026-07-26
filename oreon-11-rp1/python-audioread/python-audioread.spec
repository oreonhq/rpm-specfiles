%global source0_hash ac5460a5498c48bdf2e8e767402583a4dcd13f4414d286f42ce4379e8b35066d

Summary:        Multi-library, cross-platform audio decoding in Python
Name:           python-audioread
Version:        3.0.1
Release:        12%{?dist}
License:        MIT
URL:            http://pypi.python.org/pypi/audioread/
Source0:        https://files.pythonhosted.org/packages/source/a/audioread/audioread-%{version}.tar.gz
Patch0:         0001-Remove-legacy-sound-modules-absent-in-Python-3.13.patch
BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-gobject
BuildRequires:  /usr/bin/ffmpeg
%global _description \
Decode audio files using whichever backend is available. Among\
currently supports backends are\
 o Gstreamer via PyGObject\
 o MAD via the pymad bindings\
 o FFmpeg or Libav via its command-line interface\
 o The standard library wave, aifc, and sunau modules
%description %_description

%package    -n  python3-audioread
Summary:        Multi-library, cross-platform audio decoding in Python
Requires:       python3-gobject
Requires:       (/usr/bin/ffmpeg or (gstreamer1 and gstreamer1-plugins-base and gstreamer1-plugins-good))
%{?python_provide:%python_provide python3-audioread}
%description -n python3-audioread %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n audioread-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%check
%tox

%files -n python3-audioread
%doc README.rst decode.py
%{python3_sitelib}/audioread/
%{python3_sitelib}/audioread-*.dist-info/

%changelog
%autochangelog
