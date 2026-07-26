%global source0_hash 42984018210fdbe4d27d88c770608480dabfb72a3acdefb0af42aef9c652abea

%global	repoid		60172
%global	xyzsh_min_ver	1.5.8
%undefine	_docdir_fmt

Name:			mfiler4
Version:		1.3.1
Release:		31%{?dist}
Summary:		2 pane file manager with a embedded shell

# SPDX confirmed
License:		MIT
URL:			http://sourceforge.jp/projects/mfiler4/
Source0:		http://dl.sourceforge.jp/mfiler4/%{repoid}/%{name}-%{version}.tgz
# -Werror=format-security
Patch0:		mfiler4-1.3.1-format.patch
# -Werror=implicit-function-declaration
Patch1:		mfiler4-1.3.1-implicit-function-declaration.patch

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	cmigemo-devel
BuildRequires:	ncurses-devel
BuildRequires:	oniguruma-devel
BuildRequires:	readline-devel
BuildRequires:	xyzsh-devel >= %{xyzsh_min_ver}
# write xyzsh dependency explicitly
Requires:		xyzsh >= %{xyzsh_min_ver}

%description
mfiler4 is a 2pane file manager with a embedded shell.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Kill -O3
sed -i.optflags \
	-e 's|-O3|-O2|' \
	configure

# Kill -Werror
sed -i.werror \
	-e 's|-Werror||' \
	configure Makefile.in

# Change docdir
sed -i.docdir \
	-e '/^CFLAGS=.*DATAROOTDIR=/s|doc/mfiler4/|doc/mfiler4-%{version}/|' \
	configure

# Don't strip binary
# Keep timestamp
sed -i.bak \
	-e 's|install -m |install -p -m |' \
	-e 's|install -s |install |' \
	Makefile.in

# Umm...
sed -i.inst \
	 -e 's|USAGE.ja |USAGE.ja.txt |' \
	-e 's|USAGE |USAGE.txt |' \
	Makefile.in

%build
%configure \
	--bindir=%{_libexecdir}/%{name}/ \
	--with-migemo \
	--with-system-migemodir=%{_datadir}/cmigemo/

make %{?_smp_mflags} -k \
	CC="gcc %optflags -Werror=implicit-function-declaration" \
	docdir=%{_datadir}/doc/%{name}-%{version}

%install
make install \
	DESTDIR=%{buildroot} \
	docdir=%{_datadir}/doc/%{name}-%{version}

mkdir %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
export PATH=%{_libexecdir}/%{name}:\${PATH}
exec %{_libexecdir}/%{name}/%{name} "\$@"
EOF
chmod 0755 %{buildroot}%{_bindir}/%{name}

%files
%doc	AUTHORS
%lang(ja)	%doc	CHANGELOG
%license	LICENSE
%doc	README
%lang(ja)	%doc	README.ja
%lang(ja)	%doc	USAGE.ja.txt
%doc	USAGE.txt

%dir	%{_sysconfdir}/%{name}
%config(noreplace)	%{_sysconfdir}/%{name}/*.xyzsh

%{_bindir}/%{name}
%dir	%{_libexecdir}/%{name}
%{_libexecdir}/%{name}/%{name}
%{_libexecdir}/%{name}/mattr

%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
