%global source0_hash 884ef4a37013d968e161cc736c344eea093cf25f386b4ebb6279111acd145af6

Name:           wavextract
Version:        1.0.0
Release:        38%{?dist}
Summary:        Program for extracting embedded audio data from JPEG images
Summary(pl):    Program do wyciągania zagnieżdżonych danych audio z plików JPEG
License:        GPL-2.0-or-later
URL:            http://developer.berlios.de/projects/wavextract
Source0:        http://download.berlios.de/wavextract/%name-%version.tar.gz
Patch0:         wavextract-1.0.0-pillow.patch
Patch1:         python3.patch
BuildArch:      noarch
BuildRequires:  python3-devel
Requires:       python3 python3-imaging

%description
Program for extracting embedded audio data from JPEG images.

%description -l pl
Program do wyciągania zagnieżdżonych danych audio z plików JPEG.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}
%patch -P 0 -p1
%patch -P 1 -p0
%py3_shebang_fix ./wavextract

%build
#nothing to build

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%license COPYING
%doc README
%{_bindir}/%{name}

%changelog
%autochangelog
