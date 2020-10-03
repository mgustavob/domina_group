class profileForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
