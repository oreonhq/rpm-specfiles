%global source0_hash b6701254d88412bc5d2db869037745f65f94b900b59184157d072f35832c1111

Name:           disktype
Version:        9
Release:        47%{?dist}
Summary:        Detect the content format of a disk or disk image

License:        MIT
URL:            http://disktype.sourceforge.net/
Source0:        http://downloads.sourceforge.net/disktype/disktype-9.tar.gz

Patch0:         eju2014-disktype.patch

BuildRequires:  gcc
BuildRequires:  libewf-devel
BuildRequires:  make

%description
The purpose of disktype is to detect the content format of a disk or disk
image. It knows about common file systems, partition tables, and boot codes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
sed -i '/CFLAGS   =/d' Makefile
sed -i '/LDFLAGS  =/d' Makefile
%make_build CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="$RPM_LD_FLAGS" LIBEWF=1

%install
mkdir -p %{buildroot}{%{_bindir},%{_mandir}/man1}
install -m 755 disktype %{buildroot}%{_bindir}
install -p -m 644 disktype.1 %{buildroot}%{_mandir}/man1

%files
%doc HISTORY TODO
%license LICENSE
%{_bindir}/disktype
%{_mandir}/man1/disktype.1*

%changelog
%autochangelog
