Name:           chef-deregistration-manager
Version:        1.0.2
Release:        1%{?dist}
Summary:        Deregistration manager for chef. Useful when using AWS autoscaling.

Group:          Misc
License:        Unknown
URL:            https://github.com/laghoule/chef-deregistration-manager
Source0:        %{name}-%{version}.tar.gz
Buildarch:      noarch
BuildRequires:  python-setuptools
Requires:       python-boto, python-configobj, python-chef

%description
Queue Based Chef Client Deregistration for the Cloud

%prep
%setup -q

%build

%install
%{__python} setup.py install --root=%{buildroot}

%clean
rm -rf "${RPM_BUILD_ROOT}"

%files
%defattr(-,root,root,-)
/opt/chef-registration
/etc/chef-registration/client/example.cfg
/etc/chef-registration/server/example.cfg
/etc/init.d/registration-client
/etc/init.d/registration-server

%changelog
