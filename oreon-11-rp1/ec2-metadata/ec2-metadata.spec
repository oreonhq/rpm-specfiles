%global source0_hash none

Name:           ec2-metadata
Version:        0.1.1
Release:        24%{?dist}
Summary:        EC2 instance metadata query tool 

# note web site says "Apache License 2.0", but code actually bears
# an MIT-style license.
License:        MIT
URL:            http://aws.amazon.com/code/1825
Source0:        http://s3.amazonaws.com/ec2metadata/ec2-metadata

Requires:       bash, curl

BuildArch:      noarch

%description
A simple bash script that uses curl to query the EC2 instance metadata from
within an instance running in Amazon EC2 or another cloud provider with a
compatible metadata service.
 
%prep
# none

%build
# none

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 %{SOURCE0} $RPM_BUILD_ROOT/%{_bindir}/

%files
%defattr(755, root, root, -)
%{_bindir}/%{name}

%changelog
%autochangelog
