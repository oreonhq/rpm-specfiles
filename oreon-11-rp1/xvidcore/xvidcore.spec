# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash aeeaae952d4db395249839a3bd03841d6844843f5a4f84c271ff88f7aa1acff7
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global sovermajor 4

Name:           xvidcore
Version:        1.3.7
Release:        1%{?dist}
Summary:        MPEG-4 Simple and Advanced Simple Profile codec
License:        GPL-2.0-or-later
URL:            https://www.xvid.com/
Source0:        https://downloads.xvid.com/downloads/%{name}-%{version_no_tilde}.tar.bz2
Patch0:         %{name}-c23.patch
Patch1:         0001-Add-CET-enabling-note.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  make
%ifarch x86_64
BuildRequires:  nasm >= 2.0
%endif

%description
The Xvid video codec implements MPEG-4 Simple Profile and Advanced Simple
Profile standards. It permits compressing and decompressing digital video
in order to reduce the required bandwidth of video data for transmission
over computer networks or efficient storage on CDs or DVDs. Due to its
unrivalled quality Xvid has gained great popularity and is used in many
other GPLed applications, like e.g. Transcode, MEncoder, MPlayer, Xine and
many more.

%package        devel
Summary:        Development files for the Xvid video codec
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
This package contains header files, static library and API
documentation for the Xvid video codec.

%prep
%oreon_sha256
%autosetup -p1 -n %{name}
chmod -x examples/*.pl
for file in AUTHORS ChangeLog; do
    iconv -f ISO-8859-1 -t UTF-8 -o $file.new $file && \
    touch -r $file $file.new && \
    mv $file.new $file
done
for file in ChangeLog; do
 sed "s|\r||g" $file > $file.new && \
 touch -r $file $file.new && \
 mv $file.new $file
done
%{__sed} -i -e 's|@$(|$(|g' build/generic/Makefile
%{__sed} -i -e 's|644 $(BUILD_DIR)/$(SHARED_LIB)|755 $(BUILD_DIR)/$(SHARED_LIB)|g' build/generic/Makefile

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
%doc CodingStyle TODO examples/
%{_includedir}/xvid.h
%{_libdir}/libxvidcore.so

%changelog
%autochangelog
