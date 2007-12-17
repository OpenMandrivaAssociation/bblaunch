%define name bblaunch
%define version 0.0.3
%define release %mkrel 3

Summary: An application launcher for Blackbox type window managers
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://folk.uio.no/~steingrd/%{name}-%{version}.tar.bz2
Source1: %{name}.1
Patch0: bblaunch-0.0.3.typo.patch.bz2
License: GPL
Group: Graphical desktop/Other
Url: http://blackboxwm.sourceforge.net/
BuildRequires: X11-devel

%description
bblaunch is an application launcher that lets you set certain blackbox related
attributes on the launched program.  You can use it to run an application with
no decorations, to immediately have it sent to a specific workspace, to have it
visible on all workspaces and so on and so on.

%prep
%setup -q
%patch0 -p1 -b .typo

%build
# (blino) the default -O2 optimization makes bblaunch segfault
CFLAGS="$RPM_OPT_FLAGS -O0"%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
install -d -m 755 ${RPM_BUILD_ROOT}%{_mandir}/man1/
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_mandir}/man1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
