%global source0_hash fd3db00278caecd94b3802e1f903bf235a7137511ac0a450b31d855e3a52917b
%global ALTERNATIVES %{_bindir}/alternatives
%global version_schily 2024-03-21
%global components libschily libdeflt libmdigest libfind librmt rmt star
Name:           star
Version:        %(echo %version_schily | tr '-' '.')
Release:        1%{?dist}
Summary:        An archiving tool with ACL support
License:        CDDL-1.0 AND BSD-2-Clause AND BSD-3-Clause AND BSD-4-Clause AND LicenseRef-Public-Domain
URL:            https://codeberg.org/schilytools/schilytools
Source0:        https://codeberg.org/schilytools/schilytools/archive/2024-03-21.tar.gz#/schily-2024-03-21.tar.gz
Patch1:         star-1.5.2-rmt-rh-access.patch
Patch2:         star-2024.03.21-use-ssh-by-default.patch	
Patch3:         star-2024.03.21-manpagereferences.patch
Patch4:         star-2024.03.21-bufferoverflow.patch
ExcludeArch:    %{ix86}
Provides:       star = %{version}-%{release}
Obsoletes:      star <= 1.6
Provides:       spax = %{version}-%{release}
Obsoletes:      spax <= 1.6
Provides:       scpio = %{version}-%{release}
Obsoletes:      scpio <= 1.6
Requires(post):  %{ALTERNATIVES}
Requires(preun): %{ALTERNATIVES}
# oreon:deps
BuildRequires:  e2fsprogs-devel
BuildRequires:  gcc-c++
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libcap-devel
BuildRequires:  libselinux-devel
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
if [ %{_libdir} != %{_prefix}/lib ]; then
    mkdir -p %{buildroot}%{_libdir}
    mv %{buildroot}%{_prefix}/lib/lib*.so.* %{buildroot}%{_libdir}
fi
chmod 755 %{buildroot}%{_libdir}/lib*.so* %{buildroot}%{_bindir}/*
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
%oreon_autofiles rmt usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

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
%global ALT_NAME                pax
%global ALT_LINK                %{_bindir}/pax
%global ALT_SL1_NAME            pax-man
%global ALT_SL1_LINK            %{_mandir}/man1/pax.1.gz
%global ALT_PATH                %{_bindir}/spax
%global ALT_SL1_PATH            %{_mandir}/man1/spax.1.gz
%post

%{ALTERNATIVES} \
    --install   %{ALT_LINK}     %{ALT_NAME}     %{ALT_PATH}     66 \
    --slave     %{ALT_SL1_LINK} %{ALT_SL1_NAME} %{ALT_SL1_PATH}
%preun

if [ $1 -eq 0 ]; then
    %{ALTERNATIVES} --remove %{ALT_NAME} %{ALT_PATH}
fi
%files -f %{oreon_filedir}/main.list
%files -n rmt -f %{oreon_filedir}/rmt.list
%files -n star-libs -f %{oreon_filedir}/star-libs.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2024.03.21-1
- Import
