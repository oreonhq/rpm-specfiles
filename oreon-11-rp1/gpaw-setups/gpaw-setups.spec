%global source0_hash 964c81cc28f7f91a4686d3d3182c4ebda30efb09d3f96b7f95eae3146499c110
Name:			gpaw-setups
Version:		24.11.0
Release:        1%{?dist}
Summary:        Atomic GPAW setups
License:		GPL-3.0-or-later
URL:			https://wiki.fysik.dtu.dk/gpaw/
Source0:        https://wiki.fysik.dtu.dk/gpaw-files/%{name}-%{version}.tar.gz
BuildArch:		noarch
# oreon:deps

# /oreon:deps
%description
Atomic GPAW setups. A setup is to the PAW method what
a pseudo-potential is to the pseudo-potential method.

%prep

%setup -q -n %{name}-%{version}

%build

cat <<EOF > %{name}.sh
PA=%{_datadir}/%{name}
case \$GPAW_SETUP_PATH in
*\${PA}*);;
*) GPAW_SETUP_PATH=\${PA};;
esac
export GPAW_SETUP_PATH
EOF
cat <<EOF > %{name}.csh
set PA=%{_datadir}/%{name}
if (\$?GPAW_SETUP_PATH) then
if ("\$GPAW_SETUP_PATH" !~ *\${PA}*) then
	setenv GPAW_SETUP_PATH \${PA}
endif
else
setenv GPAW_SETUP_PATH \${PA}
endif
unset PA
EOF
%install
mkdir -p %{buildroot}%{_datadir}/%{name}
install -p -m 444 *.{gz,pckl,txt} %{buildroot}%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
install -p -m 444 %{name}*.*sh $RPM_BUILD_ROOT%{_sysconfdir}/profile.d
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
