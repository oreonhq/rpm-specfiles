%global ALTERNATIVES %{_bindir}/alternatives
%global version_schily 2024-03-21

# Use a specific order for building as libraries are linked to each other:
%global components libschily libdeflt libmdigest libfind librmt rmt star
Name:           star
Version:        %(echo %version_schily | tr '-' '.')
Release:        %autorelease 
Summary:        An archiving tool with ACL support

# libschily: CDDL-1.0 AND BSD-3-Clause AND BSD-4-Clause
# libdeflt: CDDL-1.0
# libmdigest: BSD-2-Clause AND BSD-3-Clause AND LicenseRef-Public-Domain
# libfind: CDDL-1.0
# librmt: CDDL-1.0
# rmt: CDDL-1.0
# star: CDDL-1.0 AND BSD-3-Clause

License:        CDDL-1.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND LicenseRef-Public-Domain
URL:            https://codeberg.org/schilytools/schilytools

Source0:        https://codeberg.org/schilytools/schilytools/archive/2024-03-21.tar.gz#/schily-2024-03-21.tar.gz

# Allow rmt to access all files.
# ~> downstream
# ~> #968980
Patch1:         star-1.5.2-rmt-rh-access.patch
# Use ssh rather than rsh by default
# ~> downstream
# ~> related to #968980
Patch2:         star-2024.03.21-use-ssh-by-default.patch	
# Fix some invalid manpage references (#624612)
Patch3:         star-2024.03.21-manpagereferences.patch
# Prevent buffer overflow for filenames with length of 100 characters (#556664)
# Although I couldn't replicate it with 2024.03.21-4, candidate for removal
Patch4:         star-2024.03.21-bufferoverflow.patch
# oreon url source checksums begin
%global source0_sha256 4d66bf35a5bc2927248fac82266b56514fde07c1acda66f25b9c42ccff560a02
%global source0_file 2024-03-21.tar.gz
# oreon url source checksums end

BuildRequires:  gcc-c++
BuildRequires:  libattr-devel libacl-devel libselinux-devel libcap-devel
BuildRequires:  make e2fsprogs-devel
BuildRequires:  sed

# drop i686 support ()
ExcludeArch:    %{ix86}

Provides:       star = %{version}-%{release}
Obsoletes:      star <= 1.6
Provides:       spax = %{version}-%{release}
Obsoletes:      spax <= 1.6
Provides:       scpio = %{version}-%{release}
Obsoletes:      scpio <= 1.6

Requires(post):  %{ALTERNATIVES}
Requires(preun): %{ALTERNATIVES}

%description
Star saves many files together into a single tape or disk archive,
and can restore individual files from the archive. Star supports ACL.

%package -n     rmt
Summary:        Provides certain programs with access to remote tape devices
Provides:       rmt = %{version}-%{release}
Epoch:          2
Obsoletes:      rmt <= 1.6

%description -n rmt
The rmt utility provides remote access to tape devices for programs
like dump (a filesystem backup program), restore (a program for
restoring files from a backup), and tar (an archiving program)

%package libs
Summary:        Libraries for %{name}
Provides:       star-libs = %{version}-%{release}
Obsoletes:      star-libs <= 2023.09.28-1

%description libs
This package provides the shared libraries for star.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/2024-03-21.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4d66bf35a5bc2927248fac82266b56514fde07c1acda66f25b9c42ccff560a02" || { echo "oreon: Source0 SHA256 mismatch for 2024-03-21.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n schilytools

# Convert files to utf8 for german letters:
for i in \
    $(find . -name "*.1") \
    $(find . -name "*.5") \
    $(find . -name "*.8") \
    $(find . -name "README*") \
    $(find . -name "THANKS*"); do
    iconv -f iso-8859-1 $i -t utf-8 -o $i.new && mv -f $i.new $i
done

# Move rmt to bin instead of sbin
sed -i 's/sbin/bin/' rmt/Makefile
# Run star tests with LD_PRELOAD_PATH flag, specified in the check section
sed -i 's/$(SHELL)/$(SHELL) -c $(TEST_FLAGS)/' star/tests/Makefile

%build
make_command() {
  cd $i
  make %{_make_output_sync} -f Makefile \
      CPPOPTX="%{build_cxxflags} -Wno-incompatible-pointer-types -Wno-old-style-definition" \
      COPTX="%{build_cflags} -Wno-incompatible-pointer-types -Wno-old-style-definition" \
      GMAKE_NOWARN=true \
      LINKMODE="dynamic" \
      NOECHO= \
      RUNPATH= \
      LDOPTX="%build_ldflags" \
      $*
   cd -
}

for i in %{components}; do
  make_command config
  make_command %{?_smp_mflags} all
done

%install
for i in %{components}; do
  cd $i
  make -f Makefile \
      DESTDIR=%{buildroot} \
      GMAKE_NOWARN=true \
      INS_BASE=%{_prefix} \
      INS_RBASE=/ \
      LINKMODE="dynamic" \
      NOECHO= \
      RUNPATH= \
      install
  cd -
done

mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}
mkdir -p ${RPM_BUILD_ROOT}%{_pkgdocdir}
ln -s %{_bindir}/rmt ${RPM_BUILD_ROOT}%{_sysconfdir}/rmt

# Move libraries to the appropriate place on 64 bit arches
if [ %{_libdir} != %{_prefix}/lib ]; then
    mkdir -p %{buildroot}%{_libdir}
    mv %{buildroot}%{_prefix}/lib/lib*.so.* %{buildroot}%{_libdir}
fi

# Make binaries executable
chmod 755 %{buildroot}%{_libdir}/lib*.so* %{buildroot}%{_bindir}/*

# XXX Nuke unpackaged files.
( cd ${RPM_BUILD_ROOT}
  rm -fv .%{_bindir}/mt
  rm -fv .%{_bindir}/smt
  rm -fv .%{_bindir}/tartest
  rm -fv .%{_bindir}/tar
  rm -fv .%{_bindir}/gnutar
  rm -fv .%{_bindir}/star_fat
  rm -fv .%{_bindir}/star_sym
  rm -fv .%{_bindir}/suntar
  rm -fv .%{_sysconfdir}/default/star
  rm -rfv .%{_prefix}%{_sysconfdir}
  rm -rfv .%{_prefix}/include
  rm -rfv .%{_prefix}/lib # hard-wired intently
  rm -rfv .%{_mandir}/man3
  rm -rfv .%{_mandir}/man5/{makefiles,makerules}.5*
  rm -rfv .%{_mandir}/man1/{tartest,gnutar,smt,mt,suntar,match}.1*
  rm -rfv .%{_docdir}/star/testscripts
  rm -rfv .%{_docdir}/star/TODO
  rm -rfv .%{_libdir}/*.so
  rm -rfv .%{_docdir} #install documents directly in the files section
)

%global general_docs \
%dir %{_pkgdocdir} \

%check
for i in %{components}; do
  cd $i
  make -f Makefile \
      GMAKE_NOWARN=true \
      LINKMODE="dynamic" \
      NOECHO= \
      RUNPATH= \
      TEST_FLAGS='LD_LIBRARY_PATH=%{buildroot}%{_libdir}' \
      tests
  cd -
done

# "desired" alternative constants
%global ALT_NAME                pax
%global ALT_LINK                %{_bindir}/pax
%global ALT_SL1_NAME            pax-man
%global ALT_SL1_LINK            %{_mandir}/man1/pax.1.gz

# "local" alternative constants
%global ALT_PATH                %{_bindir}/spax
%global ALT_SL1_PATH            %{_mandir}/man1/spax.1.gz

%post
%{ALTERNATIVES} \
    --install   %{ALT_LINK}     %{ALT_NAME}     %{ALT_PATH}     66 \
    --slave     %{ALT_SL1_LINK} %{ALT_SL1_NAME} %{ALT_SL1_PATH}

%preun
if [ $1 -eq 0 ]; then
    # only on pure uninstall (not upgrade)
    %{ALTERNATIVES} --remove %{ALT_NAME} %{ALT_PATH}
fi

%files -n star
%doc star/STARvsGNUTAR
%doc star/README.*
%doc star/README
%{_bindir}/star
%{_bindir}/ustar
%{_bindir}/spax
%{_bindir}/scpio
%{_mandir}/man1/star.1*
%{_mandir}/man1/ustar.1*
%{_mandir}/man5/star.5*
%doc %{_mandir}/man1/spax.1*
%doc %{_mandir}/man1/scpio.1*
%ghost %attr(0755,root,root) %verify(not md5 size mode mtime) %{ALT_LINK}
%ghost %attr(0644,root,root) %verify(not md5 size mode mtime) %{ALT_SL1_LINK}

%files -n rmt
%general_docs
%{_bindir}/rmt
%{_mandir}/man1/rmt.1*
%config(noreplace) %{_sysconfdir}/default/rmt
# This symlink is used by cpio, star, spax, scpio,... thus it is needed. Even
# if the cpio may be configured to use /bin/rmt rather than /etc/rmt, star (and
# thus spax, ..) has the lookup path hardcoded to '/etc/rmt' (it means that even
# non rpm based systems will try to look for /etc/rmt). And - the conclusion is
# it does not make sense to fight against /etc/rmt symlink ATM (year 2013).
%{_sysconfdir}/rmt

%files libs
%license COPYING GPL-2.0.txt LGPL-2.1.txt CDDL.Schily.txt AN-2024-03-21 CONTRIBUTORS
%doc README
%{_libdir}/libdeflt.so.1.0
%{_libdir}/libfind.so.4.0
%{_libdir}/libmdigest.so.1.0
%{_libdir}/libschily.so.2.0
%{_libdir}/librmt.so.1.0

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2024.03.21-1
- Import
