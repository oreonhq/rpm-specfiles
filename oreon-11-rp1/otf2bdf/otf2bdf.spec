%global source0_hash 61370b8613867386ad5b7b331a403a674e684020830b0eb83bb004a452abfada

Name:		otf2bdf
Version:	3.1
Release:	32%{?dist}
Summary:	Generate BDF bitmap fonts from OpenType outline fonts

License:	MIT
URL:		http://www.math.nmsu.edu/~mleisher/Software/otf2bdf/
Source0:	http://sofia.nmsu.edu/~mleisher/Software/%{name}/%{name}-%{version}.tgz
Patch0:		otf2bdf-configure-c99.patch

BuildRequires: make
BuildRequires:  gcc
BuildRequires:	freetype-devel

%description
otf2bdf is a command line utility that uses the FreeType 2 font
rendering library to generate BDF bitmap fonts from OpenType outline
fonts at different sizes and resolutions. This program is essentially
the same as the ttf2bdf program except that it uses FreeType 2.*, not
FreeType 1.*, has some bug fixes, and includes a new command line
parameter to print out the available encoding tables in the font.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

install -d -m 755 %{buildroot}%{_bindir}
install -p -m 755 %{name} %{buildroot}%{_bindir}

install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{name}.man %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
%autochangelog
