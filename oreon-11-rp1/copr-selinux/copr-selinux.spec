%global source0_hash c9bd2e029254738e63a9a1696dfc44645e96e5788d6bfa94902767a9dc879801

%global moduletype apps
%global modulename copr
%global selinuxbooleans httpd_enable_cgi=1 httpd_can_network_connect=1 httpd_can_sendmail=1 nis_enabled=1
# We can build 'mls' too, once this is resolved:
# https://github.com/fedora-selinux/selinux-policy-macros/pull/4
%global selinuxvariants targeted

Name:       copr-selinux
Version:    1.57
Release:    3%{?dist}
Summary:    SELinux module for COPR

License:    GPL-2.0-or-later
URL:        https://github.com/fedora-copr/copr

# Source is created by:
# git clone %%url && cd copr
# tito build --tgz --tag %%name-%%version-%%release
Source0:    %name-%version.tar.gz

BuildArch:  noarch
BuildRequires: asciidoc
BuildRequires: libxslt
BuildRequires:  perl

BuildRequires: selinux-policy-devel
%{?selinux_requires}

%description
COPR is lightweight build system. It allows you to create new project in WebUI,
and submit new builds and COPR will create yum repository from latest builds.

This package include SELinux targeted module for COPR

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build
# convert manages
a2x -d manpage -f manpage man/copr-selinux-enable.8.asciidoc
a2x -d manpage -f manpage man/copr-selinux-relabel.8.asciidoc

perl -i -pe 'BEGIN { $VER = join ".", grep /^\d+$/, split /\./, "%{version}.%{release}"; } s!\@\@VERSION\@\@!$VER!g;' %{modulename}.te
for selinuxvariant in %selinuxvariants; do
    make NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile
    bzip2 -9 %{modulename}.pp
    mv %{modulename}.pp.bz2 %{modulename}.pp.bz2.${selinuxvariant}
    make NAME=${selinuxvariant} -f %{_datadir}/selinux/devel/Makefile clean
done

%install
for selinuxvariant in %selinuxvariants; do
    install -d %{buildroot}%{_datadir}/selinux/${selinuxvariant}
    install -p -m 644 %{modulename}.pp.bz2.${selinuxvariant} \
           %{buildroot}%{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp.bz2
done
# Install SELinux interfaces
install -d %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}
install -p -m 644 %{modulename}.if \
  %{buildroot}%{_datadir}/selinux/devel/include/%{moduletype}/%{modulename}.if
install -d %{buildroot}%{_bindir}
install -p -m 755 %{name}-enable %{buildroot}%{_bindir}/%{name}-enable
install -p -m 755 %{name}-relabel %{buildroot}%{_bindir}/%{name}-relabel
install -d %{buildroot}%{_mandir}/man8
install -p -m 644 man/%{name}-enable.8 %{buildroot}/%{_mandir}/man8/
install -p -m 644 man/%{name}-relabel.8 %{buildroot}/%{_mandir}/man8/

%pre
for selinuxvariant in %selinuxvariants; do
  %selinux_relabel_pre -s $selinuxvariant
done

%post
for selinuxvariant in %selinuxvariants; do
  %selinux_modules_install -s $selinuxvariant %{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp.bz2
  %selinux_set_booleans    -s $selinuxvariant %{selinuxbooleans}
done

%postun
for selinuxvariant in %selinuxvariants; do
  %selinux_modules_uninstall -s $selinuxvariant %{modulename}
  %selinux_unset_booleans    -s $selinuxvariant %{selinuxbooleans}
done

%posttrans
for selinuxvariant in %selinuxvariants; do
  %selinux_relabel_post -s $selinuxvariant
done

%files
%license LICENSE
%{_datadir}/selinux/*/%{modulename}.pp.bz2
# empty, do not distribute it for now
%exclude %{_datadir}/selinux/devel/include/%{moduletype}/%{modulename}.if
%{_bindir}/%{name}-enable
%{_bindir}/%{name}-relabel
%{_mandir}/man8/%{name}-enable.8*
%{_mandir}/man8/%{name}-relabel.8*

%changelog
%autochangelog
