%global source0_hash none

# Package is arch'ed because of %%{_libdir}, but we do not build any
# binaries, thus there is no useful debuginfo generated.
# Disabling generation of debuginfo.
%global			debug_package	%{nil}

# Setup location of rpm-macros.
%{!?_macrosdir:%global	_macrosdir	%(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)}

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global	_pkgdocdir	%{_docdir}/%{name}-%{version}}

# Are licenses packaged using %%license?
%if 0%{?fedora} >= 21 || 0%{?rhel} >= 8
%bcond_without		license_dir
%else  # 0%%{?fedora} >= 21 || 0%%{?rhel} >= 8
%bcond_with		license_dir
%endif # 0%%{?fedora} >= 21 || 0%%{?rhel} >= 8

%global			common_description				\
This package holds the common filesystem-layout used by YaST2		\
and handles log-rotation for YaST2-logfiles.

Name:		yast2-filesystem
Version:	0.1.0
Release:	23%{?dist}
Summary:	YaST filesystem layout

License:	Unlicense
URL:		https://en.opensuse.org/Portal:YaST

# Package has no real upstream.  Spec-file was written by me,
# Björn Esser <besser82@fedoraproject.org>, and licensed as
# 'Public Domain', thus I include a matching LICENSE.txt as
# Source0 into the package.
Source0:	http://unlicense.org/UNLICENSE#/LICENSE.txt

BuildRequires:	pkgconfig(yast2-devtools)

%description
%{?common_description}

%prep
%setup -cqT

# Copy-in LICENSE-file.
%{__install} -pm 0644 %{SOURCE0} .

# Create README.txt.
echo "%{?common_description}" | %{__sed} -e '/^$/d' > README.txt

%build
# Create manifest-files.
%{__grep} -e '^%%yast_.*dir ' %{?_macrosdir}/macros.yast |		\
	%{__sed} -e '/%%yast_docdir/d' -e 's!^.*[ \t]\+!!g' |		\
	%{_bindir}/sort -u > mf.list
%{__sed} -e '/^.var.*fillup-templates$/d' -e '/^$/d' -e 's!^!%%dir !g'	\
	< mf.list | %{_bindir}/sort -u > mf.files

%install
# Create dirs from manifest.
for _dir in $(%{__cat} mf.list)
do
	_dir="$(%{_bindir}/rpm --eval ${_dir})"
	%{__mkdir} -p "%{buildroot}${_dir}"
done

# Create config for log-rotate.
%{__mkdir} -p %{buildroot}%{_sysconfdir}/logrotate.d
%{__cat} >> %{buildroot}%{_sysconfdir}/logrotate.d/%{name} << EOF
%{_localstatedir}/log/YaST2/* {
	missingok
	notifempty
	compress
	delaycompress
}
EOF

%files -f mf.files
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%dir %{_sysconfdir}/logrotate.d
%doc README.txt
%if %{with license_dir}
%license LICENSE.txt
%else  # %%{with license_dir}
%doc LICENSE.txt
%endif # %%{with license_dir}
%if "%{_libdir}" == "%{_prefix}/lib64"
%dir %{_libdir}/YaST2
%endif # "%%{_libdir}" == "%%{_prefix}/lib64"

%changelog
%autochangelog
