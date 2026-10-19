%global source0_hash a9c9966cfd9fed6c4d4895dc2de530902e736608f4033799af4fe06edf0dd438
Name:       timew
Version:    1.10.0
Release:        1%{?dist}
Summary:        Timewarrior tracks and reports time
License:    MIT
URL:        https://timewarrior.net/
Source0:        https://github.com/GothenburgBitFactory/timewarrior/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:    README.Fedora
Source2:    timew-bash-completion
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  rubygem-asciidoctor
# /oreon:deps
%description
Timewarrior is a time tracking utility that offers simple stopwatch features as
well as sophisticated calendar-base backfill, along with flexible reporting. It
is a portable, well supported and very active, Open Source project.

Please read the /usr/share/doc/timew/README.Fedora file on using the included
extensions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
cp -v %{SOURCE1} .
cp -v %{SOURCE2} completion/timew-completion.bash
chmod -x doc/holidays/*
for lib in doc/holidays/*; do
 sed '1{\@^#!/usr/bin/env python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

for lib in ext/*; do
 sed "s@^#!/usr/bin/env python3@#!%{python3}@" $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done

# Install themes in _datadir instead of _docdir
sed -i 's|DESTINATION.*|DESTINATION ${SHARE_INSTALL_PREFIX}/timew/themes/)|' doc/themes/CMakeLists.txt

%build

%cmake -DTIMEW_BINDIR=%{_bindir} -DTIMEW_DOCDIR=%{_pkgdocdir} -DTIMEW_MAN1DIR=%{_mandir}/man1/ -DTIMEW_MAN7DIR=%{_mandir}/man7/
%cmake_build
%install
%cmake_install
install -m 0755 -d $RPM_BUILD_ROOT/%{_libdir}/%{name}/
mv $RPM_BUILD_ROOT/%{_pkgdocdir}/ext $RPM_BUILD_ROOT/%{_libdir}/%{name}/ -v
chmod +x $RPM_BUILD_ROOT/%{_libdir}/%{name}/ext/*
rm -f $RPM_BUILD_ROOT/%{_docdir}/%{name}/INSTALL
rm -f $RPM_BUILD_ROOT/%{_docdir}/%{name}/LICENSE
mv -v README.Fedora $RPM_BUILD_ROOT/%{_pkgdocdir}/
install -m 0755 completion/timew-completion.bash -DT $RPM_BUILD_ROOT/%{bash_completions_dir}/timew
install -m 0755 completion/timew.fish -DT $RPM_BUILD_ROOT/%{fish_completions_dir}/timew.fish
%oreon_autofiles main

%check

make test %{_smp_mflags}
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
