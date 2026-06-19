%global source0_hash aeeaae952d4db395249839a3bd03841d6844843f5a4f84c271ff88f7aa1acff7
%global sovermajor 4

Name:           xvidcore
Version:        1.3.7
Release:        %autorelease
Summary:        MPEG-4 Simple and Advanced Simple Profile codec

License:        GPL-2.0-or-later
URL:            https://www.xvid.com/
Source0:        https://downloads.xvid.com/downloads/xvidcore-%{version}.tar.bz2

Patch0:         xvidcore-c23.patch
Patch1:         0001-Add-CET-enabling-note.patch

BuildRequires:  gcc
BuildRequires:  make
%ifarch x86_64
BuildRequires:  nasm >= 2.0
%endif

%description
The Xvid video codec implements MPEG-4 Simple Profile and Advanced Simple
Profile standards.

%package devel
Summary:        Development files for the Xvid video codec
Requires:       %{name}%{_isa} = %{version}-%{release}

%description devel
Development files for the Xvid video codec.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}
chmod -x examples/*.pl
for file in AUTHORS ChangeLog; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && touch -r $file $file.new && mv $file.new $file
done
for file in ChangeLog; do
 sed "s|\r||g" $file > $file.new && touch -r $file $file.new && mv $file.new $file
done
sed -i -e 's|@$(|$(|g' build/generic/Makefile
sed -i -e 's|644 $(BUILD_DIR)/$(SHARED_LIB)|755 $(BUILD_DIR)/$(SHARED_LIB)|g' build/generic/Makefile

%build
cd build/generic
%configure \
%ifarch %{ix86}
  --disable-assembly
%endif
%make_build LDFLAGS+="%{?build_ldflags}"

%install
%make_install -C build/generic
find %{buildroot} -name "*.a" -delete

%files
%doc README AUTHORS ChangeLog
%license LICENSE
%{_libdir}/libxvidcore.so.%{sovermajor}{,.*}

%files devel
%{_includedir}/xvid.h
%{_libdir}/libxvidcore.so

%changelog
%autochangelog
