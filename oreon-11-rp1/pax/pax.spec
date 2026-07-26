%global source0_hash ac3c06048e02828077cf7757d3d142241429238893b91d529af29a2e8cc5623b

%global ALTERNATIVES            %{_sbindir}/alternatives

Summary: POSIX File System Archiver
Name: pax
Version: 3.4
Release: 49%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD

# 2018-07-24 upstream maintainer contacted about non-working URLs
# 2020-06-02 moved upstream URLs to point to fedora git as upstream will not host it anymore
URL:    https://src.fedoraproject.org/rpms/%{name}

#use Linux PATH_MAX (4092) for maximum PATHLENGTH instead of pax default 3072
Patch0: pax-3.0-PATHMAX.patch

#fix bug with archiving files of filename length exactly 100 chars
Patch1: pax-3.4-abs100.patch

#do not truncate names when extracting
Patch2: pax-3.4-rdtruncate.patch

#do not fail with gcc-4.6+
Patch3: pax-gcc46.patch

# manpage edits - s/pax/opax/, add cross references
Patch4: pax-3.4-manpage.patch

# Remove -Werror and fix one soon-to-be-issue warning (rhbz#1424041)
Patch5: pax-3.4-disable-Werror.patch

# multiple definition and FALLTHROUGH
Patch6: pax-3.4-gcc10.patch

Requires(post):  %{ALTERNATIVES}
Requires(preun): %{ALTERNATIVES}

BuildRequires: make
BuildRequires: gcc

%description
The 'pax' utility is the POSIX standard archive tool.  It supports the two most
common forms of standard Unix archive (backup) files - CPIO and TAR.

# "desired" alternative constants
%global ALT_NAME                pax
%global ALT_LINK                %{_bindir}/pax
%global ALT_SL1_NAME            pax-man
%global ALT_SL1_LINK            %{_mandir}/man1/pax.1.gz

# "local" alternative constants ("opax" - OpenBSD pax)
%global ALT_PATH                %{_bindir}/opax
%global ALT_SL1_PATH            %{_mandir}/man1/opax.1.gz

# helpers for alternatives
%global ALT_MAN_ORIG            %{_mandir}/man1/pax.1
%global ALT_MAN_NEW             %{_mandir}/man1/opax.1

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mv %{buildroot}%{ALT_LINK} %{buildroot}%{ALT_PATH}
mv %{buildroot}%{ALT_MAN_ORIG} %{buildroot}%{ALT_MAN_NEW}
ln -s %{ALT_PATH} %{buildroot}%{ALT_LINK}
ln -s %{ALT_MAN_NEW} %{buildroot}%{ALT_MAN_ORIG}

%files
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README THANKS
%{ALT_PATH}
%doc %{ALT_SL1_PATH}
%ghost %verify(not md5 size mode mtime) %{ALT_LINK}
%ghost %verify(not md5 size mode mtime) %{ALT_SL1_LINK}

%post
# We need to remove old /usr/bin/pax binary and manpage because the following
# 'update-alternatives' step does not do it itself.  We may remove this once we
# are sure that pax >= 3.4-21 is installed on the system.
for i in "%{ALT_LINK}" "%{ALT_SL1_LINK}"; do
    test -f "$i" && test ! -h "$i" && rm -rf "$i"
done

%{ALTERNATIVES} \
    --install   %{ALT_LINK}     %{ALT_NAME}     %{ALT_PATH}     33 \
    --slave     %{ALT_SL1_LINK} %{ALT_SL1_NAME} %{ALT_SL1_PATH} \

%preun
if [ $1 -eq 0 ]; then
    # only on pure uninstall (not upgrade)
    %{ALTERNATIVES} --remove %{ALT_NAME} %{ALT_PATH}
fi

%changelog
%autochangelog
