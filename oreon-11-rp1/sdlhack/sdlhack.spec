%global source0_hash 21537005dc0b26e8c2742005f4bf58e9ae8ec75c9635917f0f1ade85d35070ba

Name:           sdlhack
Version:        1.4
Release:        23%{?dist}
Summary:        Force full-screen games to minimize
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.jspenguin.org/software/sdlhack/
Source0:        http://jspenguin.org:81/software/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.1
BuildRequires:  gcc
BuildRequires:  SDL-devel

%description
SDLHack is a wrapper for SDL which lets you force full-screen games to minimize.
It also allows you to disable joystick detection. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Change the path of the library since we install it in a private libdir
sed -i 's|lib%{name}.so|%{_libdir}/%{name}/lib%{name}.so|g' sdlhack

sed -i 's|lib%{name}-i386.so|lib%{name}.so|g;s|lig%{name}-x86_64.so|lib%{name}.so|g' build

# Remove any prebuilt lib
rm -f *.so

%build
export CFLAGS="-v %{optflags}"
bash build

%install
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name},%{_mandir}/man1}
install -Dpm 755 %{name} $RPM_BUILD_ROOT%{_bindir}
# Install libsdlhack.so in a privatelib rather than system wide one since it is gonna
# be used only with this program
install -Dpm 755 lib%{name}.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install -Dpm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%files
%doc README
%license COPYING
%{_bindir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/lib%{name}.so
%{_mandir}/man1/%{name}.1.gz

%changelog
%autochangelog
