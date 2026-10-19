%global source0_hash b5065838cbac452dfc855ba6e6e031481ad2c68406f70d21ead9321374653e6c
%global			debug_package	%{nil}
%{!?_macrosdir:%global	_macrosdir	%(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)}
%{!?_pkgdocdir:%global	_pkgdocdir	%{_docdir}/%{name}-%{version}}
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8 || 0%{?oreon} >= 11
%bcond_without		license_dir
%else  # 0%%{?fedora} >= 21 || 0%%{?rhel} >= 8
%bcond_with		license_dir
%endif # 0%%{?fedora} >= 21 || 0%%{?rhel} >= 8
%global			common_description				\
This package holds the common filesystem-layout used by YaST2		\
and handles log-rotation for YaST2-logfiles.
Name:		yast2-filesystem
Version:	0.1.0
Release:        1%{?dist}
Summary:        YaST filesystem layout
License:	Unlicense
URL:		https://en.opensuse.org/Portal:YaST
Source0:        http://unlicense.org/UNLICENSE#/LICENSE.txt
# oreon:deps
BuildRequires:  pkgconfig(yast2-devtools)
# /oreon:deps
%description
%{?common_description}

%prep

%setup -cqT

# Copy-in LICENSE-file.
%{__install} -pm 0644 %{SOURCE0} .

# Create README.txt.
echo "%{?common_description}" | %{__sed} -e '/^$/d' > README.txt

%build

%{__grep} -e '^%%yast_.*dir ' %{?_macrosdir}/macros.yast |		\
	%{__sed} -e '/%%yast_docdir/d' -e 's!^.*[ \t]\+!!g' |		\
	%{_bindir}/sort -u > mf.list
%{__sed} -e '/^.var.*fillup-templates$/d' -e '/^$/d' -e 's!^!%%dir !g'	\
	< mf.list | %{_bindir}/sort -u > mf.files
%install
for _dir in $(%{__cat} mf.list)
do
	_dir="$(%{_bindir}/rpm --eval ${_dir})"
	%{__mkdir} -p "%{buildroot}${_dir}"
done
%{__mkdir} -p %{buildroot}%{_sysconfdir}/logrotate.d
%{__cat} >> %{buildroot}%{_sysconfdir}/logrotate.d/%{name} << EOF
%{_localstatedir}/log/YaST2/* {
	missingok
	notifempty
	compress
	delaycompress
}
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
