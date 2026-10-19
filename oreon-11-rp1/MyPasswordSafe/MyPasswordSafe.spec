%global source0_hash 9df8f08df09d24725b752243b67782e3115c9f3ae4153f8035123d908678dde7
%define         datever 20061216
Name:           MyPasswordSafe
Version:        0.6.7
Release:        1%{?dist}
Summary:        A graphical password management tool
License:        GPL-2.0-or-later
URL:            http://www.semanticgap.com/myps/
Source0:        http://www.semanticgap.com/myps/release/%{name}-20061216.src.tgz
Source1:        MyPasswordSafe.desktop
Patch0:         MyPasswordSafe-20061216-use-system-uuid.patch
Patch1:         MyPasswordSafe-20061216-gcc43.patch
Patch2:         MyPasswordSafe-20090425-gcc44.patch
Patch3:         MyPasswordSafe-20061216-fix-off-by-one.patch
Patch4:         MyPasswordSafe-20061216-stack-trash.patch
Patch5:         MyPasswordSafe-20061216-unsigned-convert.patch
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libXScrnSaver-devel
BuildRequires:  make
BuildRequires:  qt3-devel
BuildRequires:  uuid-devel
# /oreon:deps
%description
MyPasswordSafe is a straight-forward, easy-to-use password manager that
maintains compatibility with Password Safe files. MyPasswordSafe has the
following features:

* Safes are encrypted when they are stored to disk.
* Passwords never have to be seen, because they are copied to the clipboard
* Random passwords can be generated.
* Window size, position, and column widths are remembered.
* Passwords remain encrypted until they need to be decrypted at the dialog
  and file levels.
* A safe can be made active so it will always be opened when MyPasswordSafe
  starts.
* Supports Unicode in the safes
* Languages supported: English and French

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{datever}

# Use the system installed ossp-uuid lib
%patch -P0 -p1 -b .use-system-uuid.patch

# Fix regressions due to stricter GCC 4.3 checking
%patch -P1 -p1 -b .gcc43

# GCC 4.4 patch
%patch -P2 -b .gcc44

# Fix off-by-one in EncryptedString::get
%patch -P3 -p1 -b off-by-one

# Fix stack trashing due to wrong array size calculations
%patch -P4 -p1 -b stack-trash

# Fix compiler warnings for narrowing to char
%patch -P5 -p1 -b unsigned-convert

%build

unset QTDIR || : ; . /etc/profile.d/qt.sh
make %{?_smp_mflags} PREFIX=%{_prefix}
%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT%{_prefix}
rm -rf $RPM_BUILD_ROOT%{_prefix}/share/doc
desktop-file-install \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications    \
    %{SOURCE1}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
