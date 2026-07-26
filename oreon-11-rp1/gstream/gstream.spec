%global source0_hash 6de17adcfb5ce08b39ca0d50a4d5898091f205cfad386eb89b04e49ab2c0d449

Name:           gstream
Version:        1.6
Release:        36%{?dist}
Summary:        Simplified stream output/input for Allegro
License:        Giftware
URL:            http://allegro.molhanec.net/gstream.html
Source0:        http://allegro.molhanec.net/gstrm16.zip
BuildRequires:  allegro-devel gcc-c++ texinfo
BuildRequires: make

%description
gstream is a C++ add-on library for Allegro. Its main purpose is to provide a
simplified syntax for Allegro's keyboard and text functions for input and
output, so that you can treat a graphical mode as a console.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       allegro-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gstream16
sed -i 's/\r//g' *.h *.cc gstream gmanip README NEWS
touch -r font.dat *.h *.cc gstream gmanip
touch -r gstream._tx README NEWS

%build
make %{?_smp_mflags} -f Makefile.unx MAKEDOC=%{_bindir}/allegro-makedoc \
  OFLAGS="$RPM_OPT_FLAGS -fsigned-char -Wno-deprecated-declarations -fPIC"
rm test.o
# makefile makes a .a file, make a .so ourselves
gcc -shared -o libgstrm.so.0 -Wl,-soname,libgstrm.so.0 $RPM_OPT_FLAGS *.o
# generate man-pages too
allegro-makedoc -man foo.3 gstream._tx
sed -i 's/^.BR \(.*\) (3)/.BR gstream-\1 (3)/g' *.3
touch -r gstream._tx *.3 gstream.html gstream.inf

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_infodir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
install -m 755 libgstrm.so.0 $RPM_BUILD_ROOT%{_libdir}
ln -s libgstrm.so.0 $RPM_BUILD_ROOT%{_libdir}/libgstrm.so
install -p -m 644 gstream.h gstream gmanip.h gmanip \
  $RPM_BUILD_ROOT%{_includedir}/%{name}
install -p -m 644 %{name}.inf $RPM_BUILD_ROOT%{_infodir}/%{name}.info
for i in *.3; do
  install -p -m 644 $i $RPM_BUILD_ROOT%{_mandir}/man3/%{name}-$i
done
  
%ldconfig_scriptlets

%files
%doc README NEWS
%{_libdir}/libgstrm.so.0

%files devel
%doc %{name}.html
%{_includedir}/%{name}
%{_libdir}/libgstrm.so
%{_infodir}/%{name}.info*
%{_mandir}/man3/%{name}-*

%changelog
%autochangelog
