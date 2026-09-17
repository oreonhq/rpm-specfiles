%global source0_hash b9f5a9f66b042d059420cd7e6f951d14405476401827399204b6a23d1fec2fcf

Name:           glinf
Version:        1.0
Release:        %autorelease
Summary:        Print information about OpenGL or OpenGLES contexts

License:        MIT
URL:            https://marlam.de/glinf
Source0:        %{url}/releases/%{name}-%{version}.tar.gz
Source1:        %{url}/releases/%{name}-%{version}.tar.gz.sig
Source2:        https://marlam.de/key.txt

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gnupg2

BuildRequires:  qt5-qtbase-devel

%description
This is a simple tool that prints information about OpenGL or OpenGLES
contexts. It is roughly comparable to glewinfo or glxinfo, with the
following differences:
- it uses Qt for platform abstraction
- it focusses on modern OpenGL
- it prints implementation limits such as GL_MAX_DRAW_BUFFERS
- it omits information about GLX and visuals

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
%autochangelog
